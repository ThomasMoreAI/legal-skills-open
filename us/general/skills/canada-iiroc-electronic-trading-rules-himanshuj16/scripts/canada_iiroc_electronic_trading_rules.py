"""
canada-iiroc-electronic-trading-rules: Automated pre-trade risk and order-marking
controls for Canadian marketplaces, aligned with NI 23-103 section 3, UMIR Rule 7.1
(and Policy 7.1), and the UMIR 6.2 order designation requirements administered by
CIRO (the successor to IIROC).

The engine is deliberately stateless: aggregate exposure is supplied by the caller
on each order so the same instance can be shared across threads and processes.
"""
import logging
import math
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

logger = logging.getLogger(__name__)


class OrderSide(Enum):
    BUY = 1
    SELL = 2
    SELL_SHORT = 3


class OrderMarker(Enum):
    """
    UMIR 6.2(1)(b) regulatory order designation carried on the order.

    NONE                 - no short-related designation (long sale or ordinary purchase).
    SHORT                - "short sale" designation, UMIR 6.2(1)(b)(viii).
    SHORT_MARKING_EXEMPT - "short-marking exempt" designation, UMIR 6.2(1)(b)(ix).
    """
    NONE = "NONE"
    SHORT = "SHORT"
    SHORT_MARKING_EXEMPT = "SME"


class ViolationCode(Enum):
    FAT_FINGER_SIZE = "V01"
    FAT_FINGER_PRICE = "V02"
    MAX_CAPITAL_EXCEEDED = "V03"
    IMPROPER_SHORT_MARK = "V04"
    MISMARKED_LONG_SALE = "V05"
    IMPROPER_SME_MARK = "V06"
    INVALID_ORDER_PARAMETERS = "V07"
    REFERENCE_PRICE_UNAVAILABLE = "V08"
    AGGREGATE_OPEN_ORDER_VALUE_EXCEEDED = "V09"


@dataclass
class ComplianceResult:
    is_compliant: bool
    violations: List[ViolationCode]
    reason: str


class RegulatoryViolationError(Exception):
    """Raised by CiroPreTradeRiskEngine.enforce_order when an order is rejected."""

    def __init__(self, result: ComplianceResult) -> None:
        super().__init__(result.reason)
        self.result = result

    @property
    def violations(self) -> List[ViolationCode]:
        return self.result.violations


@dataclass
class Order:
    """
    A normalized order presented to the pre-trade gate.

    price:                  limit price in CAD, or None for a market order (no collar is
                            applied to a market order; its notional is derived from the
                            reference price instead).
    current_inventory:      position in `symbol` currently owned by the account. This is a
                            *proxy* for the UMIR concept of ownership, which is broader
                            (securities owned through an agent or trustee, plus the deemed
                            ownership provisions of UMIR 1.2). A firm whose ownership
                            definition is broader must supply the broader figure here.
    last_traded_price:      reference price used for the fat-finger collar.
    account_is_short_marking_exempt:
                            True when the account qualifies for the "short-marking exempt"
                            designation under UMIR 6.2(1)(b)(ix). Its use on a qualifying
                            account is mandatory, not optional, and it applies to purchases
                            as well as sales.
    marker:                 explicit regulatory designation. When None, the marker is
                            inferred from `side` (SELL_SHORT implies OrderMarker.SHORT).
    open_order_notional_cad:
                            caller-supplied CAD value of the account's currently unexecuted
                            (open) orders, used for the aggregate control.
    """
    order_id: str
    symbol: str
    side: OrderSide
    quantity: int
    price: Optional[float]
    current_inventory: int
    last_traded_price: float
    account_is_short_marking_exempt: bool = False
    marker: Optional[OrderMarker] = None
    open_order_notional_cad: float = 0.0

    def effective_marker(self) -> OrderMarker:
        """Resolve the designation actually carried on the order."""
        if self.marker is not None:
            return self.marker
        if self.side == OrderSide.SELL_SHORT:
            return OrderMarker.SHORT
        return OrderMarker.NONE


@dataclass
class RiskLimits:
    """
    Firm-determined pre-trade thresholds.

    Neither NI 23-103 nor UMIR prescribes numeric values; every threshold below must be
    set, documented and periodically reassessed by the marketplace participant
    (NI 23-103 s.3(5) and s.3(6)).

    max_open_order_notional_cad implements the Policy 7.1 control on the value of
    *unexecuted* orders. Leaving it None disables that control - the engine then does not
    provide it, and the firm must implement it elsewhere.
    """
    max_order_quantity: int = 100_000
    max_order_value_cad: float = 1_000_000.0
    max_price_deviation_pct: float = 0.05  # 5%
    max_open_order_notional_cad: Optional[float] = None


def _is_finite_number(value: object) -> bool:
    """True only for a real, finite int/float. Rejects None, bool and non-numerics."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    return math.isfinite(value)


def _is_finite_positive(value: object) -> bool:
    return _is_finite_number(value) and value > 0


class CiroPreTradeRiskEngine:
    """
    CIRO (formerly IIROC) pre-trade risk control engine for Canadian marketplaces.

    Implements the automated pre-order-entry controls required by NI 23-103 s.3(2)-3(3)
    and UMIR Rule 7.1 / Policy 7.1: size and price parameters, credit/capital thresholds,
    a limit on the value of unexecuted orders, and the UMIR 6.2 short sale and
    short-marking exempt designation checks.

    The engine fails closed: an order whose parameters or reference price cannot be
    validated is rejected rather than passed through.
    """

    def __init__(self, limits: RiskLimits) -> None:
        self.limits = limits

    def validate_order(self, order: Order) -> ComplianceResult:
        """Evaluate `order` against all configured controls and return a result object."""
        violations: List[ViolationCode] = []
        reasons: List[str] = []

        # 0. Input sanity. A non-finite or non-positive value would silently defeat every
        #    numeric comparison below, since all comparisons against NaN evaluate False.
        if (isinstance(order.quantity, bool) or not isinstance(order.quantity, int)
                or order.quantity <= 0):
            violations.append(ViolationCode.INVALID_ORDER_PARAMETERS)
            reasons.append(f"Quantity {order.quantity!r} is not a positive integer.")
        if order.price is not None and not _is_finite_positive(order.price):
            violations.append(ViolationCode.INVALID_ORDER_PARAMETERS)
            reasons.append(f"Limit price {order.price!r} is not a finite positive number.")
        if not _is_finite_number(order.open_order_notional_cad) or order.open_order_notional_cad < 0:
            violations.append(ViolationCode.INVALID_ORDER_PARAMETERS)
            reasons.append(
                f"Open order notional {order.open_order_notional_cad!r} is not a finite "
                "non-negative number.")
        if not isinstance(order.side, OrderSide):
            violations.append(ViolationCode.INVALID_ORDER_PARAMETERS)
            reasons.append(f"Side {order.side!r} is not an OrderSide.")
        if order.marker is not None and not isinstance(order.marker, OrderMarker):
            violations.append(ViolationCode.INVALID_ORDER_PARAMETERS)
            reasons.append(f"Marker {order.marker!r} is not an OrderMarker.")
        if not isinstance(order.current_inventory, int) or isinstance(order.current_inventory, bool):
            violations.append(ViolationCode.INVALID_ORDER_PARAMETERS)
            reasons.append(f"Inventory {order.current_inventory!r} is not an integer.")

        if not _is_finite_positive(order.last_traded_price):
            # Fail closed: without a usable reference price the price collar cannot be
            # applied, and NI 23-103 s.3(3)(a) requires the price parameter check.
            violations.append(ViolationCode.REFERENCE_PRICE_UNAVAILABLE)
            reasons.append(
                f"Reference price {order.last_traded_price!r} unavailable or invalid; "
                "price collar cannot be evaluated.")

        if violations:
            return self._reject(order, violations, reasons)

        # 1. Fat finger size check (NI 23-103 s.3(3)(a) size parameter).
        if order.quantity > self.limits.max_order_quantity:
            violations.append(ViolationCode.FAT_FINGER_SIZE)
            reasons.append(f"Qty {order.quantity} exceeds max {self.limits.max_order_quantity}.")

        # 2. Credit / capital threshold check on this order's notional. A market order has
        #    no limit price, so value it at the reference price.
        valuation_price = order.price if order.price is not None else order.last_traded_price
        order_value = order.quantity * valuation_price
        if order_value > self.limits.max_order_value_cad:
            violations.append(ViolationCode.MAX_CAPITAL_EXCEEDED)
            reasons.append(
                f"Value CAD {order_value:,.2f} exceeds limit "
                f"{self.limits.max_order_value_cad:,.2f}.")

        # 3. Aggregate unexecuted-order value check (UMIR Policy 7.1).
        if self.limits.max_open_order_notional_cad is not None:
            projected = order.open_order_notional_cad + order_value
            if projected > self.limits.max_open_order_notional_cad:
                violations.append(ViolationCode.AGGREGATE_OPEN_ORDER_VALUE_EXCEEDED)
                reasons.append(
                    f"Projected open order value CAD {projected:,.2f} exceeds limit "
                    f"{self.limits.max_open_order_notional_cad:,.2f}.")

        # 4. Fat finger price collar versus the reference price. Market orders carry no
        #    limit price and are not collared here; they are constrained by the size and
        #    notional controls above.
        if order.price is not None:
            deviation = abs(order.price - order.last_traded_price) / order.last_traded_price
            if deviation > self.limits.max_price_deviation_pct:
                violations.append(ViolationCode.FAT_FINGER_PRICE)
                reasons.append(
                    f"Price {order.price} deviates {deviation:.2%} from LTP "
                    f"{order.last_traded_price}.")

        # 5. UMIR 6.2(1)(b) designation checks.
        violations.extend(self._check_designation(order, reasons))

        if violations:
            return self._reject(order, violations, reasons)

        return ComplianceResult(is_compliant=True, violations=[], reason="Approved")

    def _check_designation(self, order: Order, reasons: List[str]) -> List[ViolationCode]:
        """
        Verify the UMIR 6.2 regulatory designation.

        - An account that qualifies as short-marking exempt must mark *every* order,
          purchase or sale, "short-marking exempt", and must not additionally mark it
          "short" (UMIR 6.2(1)(b)(ix)).
        - Any other sell order for a security the account does not own must be marked
          "short" (UMIR 6.2(1)(b)(viii)).
        - A sale fully covered by owned inventory must NOT be marked short; over-marking
          is as much a misdesignation as under-marking.
        """
        violations: List[ViolationCode] = []
        marker = order.effective_marker()

        if order.account_is_short_marking_exempt:
            if marker != OrderMarker.SHORT_MARKING_EXEMPT:
                violations.append(ViolationCode.IMPROPER_SME_MARK)
                reasons.append(
                    f"Account is short-marking exempt; order carries marker {marker.value} "
                    "but UMIR 6.2(1)(b)(ix) requires the SME designation on every order.")
            return violations

        if marker == OrderMarker.SHORT_MARKING_EXEMPT:
            violations.append(ViolationCode.IMPROPER_SME_MARK)
            reasons.append("SME designation used on an account that is not short-marking exempt.")
            return violations

        if order.side == OrderSide.BUY:
            if marker != OrderMarker.NONE:
                violations.append(ViolationCode.MISMARKED_LONG_SALE)
                reasons.append(f"Buy order must not carry marker {marker.value}.")
            return violations

        if order.current_inventory < order.quantity:
            if marker != OrderMarker.SHORT:
                violations.append(ViolationCode.IMPROPER_SHORT_MARK)
                reasons.append(
                    f"Sell order for {order.quantity} but inventory is only "
                    f"{order.current_inventory}. Must be marked short (UMIR 6.2(1)(b)(viii)).")
        elif marker == OrderMarker.SHORT:
            violations.append(ViolationCode.MISMARKED_LONG_SALE)
            reasons.append(
                f"Sell order for {order.quantity} is fully covered by inventory "
                f"{order.current_inventory} and must not be marked short.")

        return violations

    def _reject(
        self, order: Order, violations: List[ViolationCode], reasons: List[str]
    ) -> ComplianceResult:
        reason = " | ".join(reasons)
        logger.warning(f"Order {order.order_id} REJECTED by CIRO Risk Engine: {reason}")
        return ComplianceResult(is_compliant=False, violations=list(violations), reason=reason)

    def enforce_order(self, order: Order) -> ComplianceResult:
        """
        Hard pre-trade gate: validate `order` and raise on any violation.

        Use this on the routing path when the caller has no branch for a rejection, so a
        non-compliant order cannot reach the marketplace through a forgotten return-value
        check. Raises RegulatoryViolationError.
        """
        result = self.validate_order(order)
        if not result.is_compliant:
            raise RegulatoryViolationError(result)
        return result
