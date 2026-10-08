"""IRC Section 1259 constructive sale engine for US taxable portfolios.

Statutory basis (26 U.S.C. Sec. 1259, enacted by the Taxpayer Relief Act of
1997):

  * Sec. 1259(a)(1) -- gain is recognized "as if such position were sold,
    assigned, or otherwise terminated at its fair market value on the date of
    such constructive sale".
  * Sec. 1259(a)(2) -- basis is adjusted for the gain recognized and the
    holding period restarts on the constructive sale date.
  * Sec. 1259(b)(1)/(b)(2) -- definition of an "appreciated financial
    position" and its exclusions (notably marked-to-market positions).
  * Sec. 1259(c)(1)(A)-(D) -- the four per se constructive sale transactions.
  * Sec. 1259(c)(1)(E) -- other transactions with substantially the same
    effect, but only "to the extent prescribed by the Secretary in
    regulations". No such regulations have been issued, so this module does
    NOT auto-classify collars, in-the-money puts, or similar structures.
  * Sec. 1259(c)(3)(A) -- the 30-day close / 60-day unhedged safe harbor.
  * Sec. 1259(c)(3)(B) -- a risk-reducing transaction entered during the
    60-day window may itself be disregarded if it satisfies (A).
  * Sec. 246(c)(4) (incorporated by Sec. 1259(c)(3)(A)(iii)) -- what counts as
    a reduction of the taxpayer's risk of loss.

This module is a deterministic compliance aid, not tax advice. It does not
decide "same or substantially identical property"; the caller asserts that by
supplying an offsetting transaction.
"""

from __future__ import annotations

import logging
import math
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List, Optional, Sequence, Tuple

logger = logging.getLogger(__name__)

# Sec. 1259(c)(3)(A)(i): closed "on or before the 30th day after the close of
# such taxable year".
SAFE_HARBOR_CLOSE_WINDOW_DAYS = 30
# Sec. 1259(c)(3)(A)(ii): "the 60-day period beginning on the date such
# transaction is closed" -- day 1 is the close date itself.
SAFE_HARBOR_UNHEDGED_DAYS = 60

# Sec. 1259(c)(1)(A)-(D). These are constructive sales by operation of the
# statute, with no implementing regulations required.
PER_SE_CONSTRUCTIVE_SALE_TYPES = {
    "SHORT_SALE": "Sec. 1259(c)(1)(A)",
    "OFFSETTING_NOTIONAL_PRINCIPAL_CONTRACT": "Sec. 1259(c)(1)(B)",
    # Alias retained for callers; the contract must still meet the
    # Sec. 1259(d)(2) definition of an offsetting notional principal contract.
    "EQUITY_SWAP": "Sec. 1259(c)(1)(B)",
    "FUTURES_CONTRACT": "Sec. 1259(c)(1)(C)",
    "FORWARD_CONTRACT": "Sec. 1259(c)(1)(C)",
    "ACQUISITION_OF_IDENTICAL_PROPERTY": "Sec. 1259(c)(1)(D)",
}

STATUS_NOT_APPLICABLE = "NOT_APPLICABLE"
STATUS_SAFE_HARBOR_QUALIFIED = "SAFE_HARBOR_QUALIFIED"
STATUS_CONSTRUCTIVE_SALE_TRIGGERED = "CONSTRUCTIVE_SALE_TRIGGERED"
STATUS_MANUAL_REVIEW_REQUIRED = "MANUAL_REVIEW_REQUIRED"


class ConstructiveSaleError(ValueError):
    """Raised when inputs cannot support a defensible Sec. 1259 determination."""


def _require_finite_positive(value: float, label: str) -> None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ConstructiveSaleError(f"{label} must be numeric, got {value!r}.")
    if not math.isfinite(float(value)):
        raise ConstructiveSaleError(f"{label} must be finite, got {value!r}.")
    if float(value) <= 0:
        raise ConstructiveSaleError(f"{label} must be strictly positive, got {value!r}.")


def _require_finite_non_negative(value: float, label: str) -> None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ConstructiveSaleError(f"{label} must be numeric, got {value!r}.")
    if not math.isfinite(float(value)):
        raise ConstructiveSaleError(f"{label} must be finite, got {value!r}.")
    if float(value) < 0:
        raise ConstructiveSaleError(f"{label} must not be negative, got {value!r}.")


@dataclass
class AppreciatedPosition:
    """A long position tested against Sec. 1259(b)(1).

    ``fair_market_value_per_share`` MUST be the fair market value on the
    potential constructive sale date -- i.e. the offsetting transaction's entry
    date -- because Sec. 1259(a)(1) measures gain at that date, not at the
    reporting date. Pass ``valuation_date`` to have the engine enforce it.

    ``is_marked_to_market`` excludes the position under Sec. 1259(b)(2)(C)
    (e.g. a Sec. 1256 contract, or securities held by a trader with a
    Sec. 475(f) mark-to-market election in effect).
    """

    symbol: str
    quantity: float
    cost_basis_per_share: float
    fair_market_value_per_share: float
    valuation_date: Optional[date] = None
    is_marked_to_market: bool = False

    def validate(self) -> None:
        if not self.symbol or not str(self.symbol).strip():
            raise ConstructiveSaleError("symbol must be a non-empty identifier.")
        _require_finite_positive(self.quantity, "quantity")
        _require_finite_non_negative(self.cost_basis_per_share, "cost_basis_per_share")
        _require_finite_non_negative(
            self.fair_market_value_per_share, "fair_market_value_per_share"
        )


@dataclass
class RiskReductionEvent:
    """A Sec. 246(c)(4) risk-of-loss reduction, incorporated by Sec. 1259(c)(3)(A)(iii).

    Covers holding an option to sell (protective put), a contractual obligation
    to sell, an open short sale of substantially identical property, or writing
    a call. ``close_date`` is required for the Sec. 1259(c)(3)(B) relief path;
    ``None`` means the risk reduction was still open.
    """

    event_type: str
    start_date: date
    close_date: Optional[date] = None
    description: str = ""

    def validate(self) -> None:
        if self.close_date is not None and self.close_date < self.start_date:
            raise ConstructiveSaleError(
                f"RiskReductionEvent close_date {self.close_date} precedes "
                f"start_date {self.start_date}."
            )


@dataclass
class OffsettingTransaction:
    """The transaction tested against Sec. 1259(c)(1).

    ``tax_year_end_date`` is the end of the taxable year *in which the
    transaction was entered into* -- Sec. 1259(c)(3)(A)(i) measures the 30-day
    deadline from "the close of such taxable year". It is not always Dec 31;
    fiscal-year filers must supply their own year end.

    ``offsetting_quantity`` is the number of shares actually offset. A partial
    hedge constructively sells only the hedged portion; ``None`` means the whole
    position is offset.
    """

    transaction_type: str
    entry_date: date
    close_date: Optional[date]
    tax_year_end_date: date
    re_hedged_during_60_days: bool = False
    offsetting_quantity: Optional[float] = None
    long_position_disposal_date: Optional[date] = None
    risk_reduction_events: Sequence[RiskReductionEvent] = field(default_factory=tuple)

    def validate(self) -> None:
        if not self.transaction_type or not str(self.transaction_type).strip():
            raise ConstructiveSaleError("transaction_type must be a non-empty string.")
        if self.close_date is not None and self.close_date < self.entry_date:
            raise ConstructiveSaleError(
                f"close_date {self.close_date} precedes entry_date {self.entry_date}."
            )
        if self.tax_year_end_date < self.entry_date:
            raise ConstructiveSaleError(
                f"tax_year_end_date {self.tax_year_end_date} precedes entry_date "
                f"{self.entry_date}; supply the year end of the taxable year in "
                "which the transaction was entered into."
            )
        if self.tax_year_end_date - self.entry_date > timedelta(days=366):
            raise ConstructiveSaleError(
                f"tax_year_end_date {self.tax_year_end_date} is more than one year "
                f"after entry_date {self.entry_date}; a taxable year cannot exceed "
                "12 months."
            )
        if (
            self.long_position_disposal_date is not None
            and self.long_position_disposal_date < self.entry_date
        ):
            raise ConstructiveSaleError(
                f"long_position_disposal_date {self.long_position_disposal_date} "
                f"precedes entry_date {self.entry_date}."
            )
        if self.offsetting_quantity is not None:
            _require_finite_positive(self.offsetting_quantity, "offsetting_quantity")
        for event in self.risk_reduction_events:
            event.validate()


@dataclass
class ConstructiveSaleResult:
    """Outcome of a Sec. 1259 evaluation.

    ``adjusted_basis_per_share`` and ``new_holding_period_start_date`` implement
    Sec. 1259(a)(2): after a constructive sale the position takes a new basis
    equal to the fair market value recognized and a fresh holding period.
    """

    status: str
    unrealized_gain: float
    realized_taxable_gain: float
    constructive_sale_date: Optional[date]
    reason: str
    statutory_citation: str = ""
    constructively_sold_quantity: float = 0.0
    adjusted_basis_per_share: Optional[float] = None
    new_holding_period_start_date: Optional[date] = None


class ConstructiveSaleRuleEngine:
    """US tax compliance engine for IRC Sec. 1259 constructive sale detection and
    the Sec. 1259(c)(3) 30-day / 60-day safe harbor audit.

    The engine is deterministic and stateless. It never guesses on transactions
    that reach Sec. 1259 only through the unwritten Sec. 1259(c)(1)(E)
    regulations; those return ``MANUAL_REVIEW_REQUIRED``.
    """

    def evaluate_transaction(
        self,
        position: AppreciatedPosition,
        offsetting: Optional[OffsettingTransaction],
    ) -> ConstructiveSaleResult:
        """Evaluate one appreciated position against one offsetting transaction.

        Raises:
            ConstructiveSaleError: if the inputs are internally inconsistent.
        """
        position.validate()

        # Validate the FMV date before any gate that could exit early: a price
        # taken on the wrong date can make an appreciated position look like a
        # loss and silently suppress a real constructive sale.
        if offsetting is not None:
            offsetting.validate()
            if (
                position.valuation_date is not None
                and position.valuation_date != offsetting.entry_date
            ):
                raise ConstructiveSaleError(
                    f"fair_market_value_per_share is dated {position.valuation_date} "
                    "but Sec. 1259(a)(1) measures gain at the constructive sale date "
                    f"{offsetting.entry_date}. Supply the FMV as of the entry date."
                )

        total_cost_basis = position.quantity * position.cost_basis_per_share
        total_fmv = position.quantity * position.fair_market_value_per_share
        unrealized_gain = total_fmv - total_cost_basis

        # Sec. 1259(b)(2): marked-to-market positions are not appreciated
        # financial positions at all, so no constructive sale can arise.
        if position.is_marked_to_market:
            return self._not_applicable(
                unrealized_gain,
                "Position is marked to market (e.g. Sec. 1256 contract or Sec. 475(f) "
                "election), so it is not an appreciated financial position.",
                "Sec. 1259(b)(2)(C)",
            )

        # Sec. 1259(b)(1): only positions that would produce gain on a sale.
        if unrealized_gain <= 0:
            return self._not_applicable(
                unrealized_gain,
                "Position is at a loss or break-even, so it is not an appreciated "
                "financial position.",
                "Sec. 1259(b)(1)",
            )

        if offsetting is None:
            return self._not_applicable(
                unrealized_gain,
                "No offsetting position established.",
                "Sec. 1259(c)(1)",
            )

        # Sec. 1259(c)(1): is this a per se constructive sale transaction?
        transaction_type = str(offsetting.transaction_type).strip().upper()
        citation = PER_SE_CONSTRUCTIVE_SALE_TYPES.get(transaction_type)
        if citation is None:
            reason = (
                f"Transaction type '{transaction_type}' is not listed in "
                "Sec. 1259(c)(1)(A)-(D). It could only be a constructive sale under "
                "Sec. 1259(c)(1)(E), which applies solely 'to the extent prescribed by "
                "the Secretary in regulations'; no such regulations have been issued. "
                "Escalate to a tax adviser rather than auto-classifying."
            )
            logger.warning("Sec. 1259 review required for %s: %s", position.symbol, reason)
            return ConstructiveSaleResult(
                status=STATUS_MANUAL_REVIEW_REQUIRED,
                unrealized_gain=round(unrealized_gain, 2),
                realized_taxable_gain=0.0,
                constructive_sale_date=None,
                reason=reason,
                statutory_citation="Sec. 1259(c)(1)(E)",
            )

        # Only the hedged portion of the position is constructively sold.
        offset_quantity = (
            position.quantity
            if offsetting.offsetting_quantity is None
            else min(float(offsetting.offsetting_quantity), position.quantity)
        )
        gain_at_risk = unrealized_gain * (offset_quantity / position.quantity)

        # Sec. 1259(c)(3)(A)(i): closed on or before the 30th day after year end.
        max_allowed_close_date = offsetting.tax_year_end_date + timedelta(
            days=SAFE_HARBOR_CLOSE_WINDOW_DAYS
        )
        if offsetting.close_date is None or offsetting.close_date > max_allowed_close_date:
            return self._triggered(
                position,
                offsetting,
                unrealized_gain,
                gain_at_risk,
                offset_quantity,
                (
                    "Offsetting position was not closed on or before the 30th day after "
                    f"the close of the taxable year ({max_allowed_close_date})."
                ),
                "Sec. 1259(c)(3)(A)(i)",
            )

        window_start = offsetting.close_date
        # A 60-day period beginning on the close date runs through close + 59 days.
        window_end = window_start + timedelta(days=SAFE_HARBOR_UNHEDGED_DAYS - 1)

        # Sec. 1259(c)(3)(A)(ii): the position must be held throughout the window.
        disposal = offsetting.long_position_disposal_date
        if disposal is not None and disposal <= window_end:
            return self._triggered(
                position,
                offsetting,
                unrealized_gain,
                gain_at_risk,
                offset_quantity,
                (
                    f"Appreciated position was disposed of on {disposal}, inside the "
                    f"60-day period {window_start} through {window_end} that the "
                    "taxpayer must hold it throughout."
                ),
                "Sec. 1259(c)(3)(A)(ii)",
            )

        # Sec. 1259(c)(3)(A)(iii), with the Sec. 1259(c)(3)(B) relief path.
        status, reason, cite = self._evaluate_risk_reduction(
            offsetting, window_start, window_end, max_allowed_close_date
        )
        if status == STATUS_MANUAL_REVIEW_REQUIRED:
            logger.warning("Sec. 1259 review required for %s: %s", position.symbol, reason)
            return ConstructiveSaleResult(
                status=STATUS_MANUAL_REVIEW_REQUIRED,
                unrealized_gain=round(unrealized_gain, 2),
                realized_taxable_gain=0.0,
                constructive_sale_date=None,
                reason=reason,
                statutory_citation=cite,
            )
        if status == STATUS_CONSTRUCTIVE_SALE_TRIGGERED:
            return self._triggered(
                position,
                offsetting,
                unrealized_gain,
                gain_at_risk,
                offset_quantity,
                reason,
                cite,
            )

        logger.info(
            "Sec. 1259(c)(3) safe harbor satisfied for %s; no gain recognized.",
            position.symbol,
        )
        return ConstructiveSaleResult(
            status=STATUS_SAFE_HARBOR_QUALIFIED,
            unrealized_gain=round(unrealized_gain, 2),
            realized_taxable_gain=0.0,
            constructive_sale_date=None,
            reason=(
                "Transaction is disregarded: closed on or before "
                f"{max_allowed_close_date}, and the position was held with no "
                f"Sec. 246(c)(4) risk reduction throughout {window_start} to "
                f"{window_end}."
            ),
            statutory_citation="Sec. 1259(c)(3)(A)",
        )

    def _evaluate_risk_reduction(
        self,
        offsetting: OffsettingTransaction,
        window_start: date,
        window_end: date,
        max_allowed_close_date: date,
    ) -> Tuple[str, str, str]:
        """Apply Sec. 1259(c)(3)(A)(iii) and the Sec. 1259(c)(3)(B) carve-out.

        Returns a ``(status, reason, citation)`` triple; ``reason`` is empty when
        the safe harbor is satisfied.
        """
        events: List[RiskReductionEvent] = [
            event
            for event in offsetting.risk_reduction_events
            if window_start <= event.start_date <= window_end
        ]

        if not events:
            # Legacy flag: an unstructured assertion that risk was reduced, with
            # no evidence that Sec. 1259(c)(3)(B) relief applies.
            if offsetting.re_hedged_during_60_days:
                return (
                    STATUS_CONSTRUCTIVE_SALE_TRIGGERED,
                    (
                        "Risk of loss was reduced during the 60-day period "
                        f"{window_start} to {window_end} and no Sec. 1259(c)(3)(B) "
                        "relief was evidenced."
                    ),
                    "Sec. 1259(c)(3)(A)(iii)",
                )
            return (STATUS_SAFE_HARBOR_QUALIFIED, "", "Sec. 1259(c)(3)(A)(iii)")

        for event in events:
            # Sec. 1259(c)(3)(B)(ii)(II): the second transaction must itself be
            # closed by the 30th day after the close of the first transaction's
            # taxable year.
            if event.close_date is None or event.close_date > max_allowed_close_date:
                return (
                    STATUS_CONSTRUCTIVE_SALE_TRIGGERED,
                    (
                        f"Risk reduction '{event.event_type}' beginning "
                        f"{event.start_date} falls inside the 60-day period "
                        f"{window_start} to {window_end} and was not closed by "
                        f"{max_allowed_close_date}, so Sec. 1259(c)(3)(B) cannot "
                        "disregard it."
                    ),
                    "Sec. 1259(c)(3)(A)(iii)",
                )

            # Sec. 1259(c)(3)(B)(ii)(III): the second transaction must itself
            # satisfy clauses (ii) and (iii) of subparagraph (A).
            second_window_end = event.close_date + timedelta(
                days=SAFE_HARBOR_UNHEDGED_DAYS - 1
            )
            disposal = offsetting.long_position_disposal_date
            if disposal is not None and disposal <= second_window_end:
                return (
                    STATUS_CONSTRUCTIVE_SALE_TRIGGERED,
                    (
                        f"Risk reduction '{event.event_type}' cannot be disregarded: "
                        f"the position was disposed of on {disposal}, inside its own "
                        f"60-day period ending {second_window_end}."
                    ),
                    "Sec. 1259(c)(3)(B)",
                )

            overlapping = [
                other
                for other in offsetting.risk_reduction_events
                if other is not event
                and event.close_date <= other.start_date <= second_window_end
            ]
            if overlapping:
                return (
                    STATUS_MANUAL_REVIEW_REQUIRED,
                    (
                        f"Risk reduction '{event.event_type}' closed {event.close_date} "
                        f"is followed by a further risk reduction on "
                        f"{overlapping[0].start_date}, inside its own 60-day period. "
                        "Sec. 1259(c)(3)(B) does not clearly permit chained relief; "
                        "escalate to a tax adviser."
                    ),
                    "Sec. 1259(c)(3)(B)",
                )

        return (STATUS_SAFE_HARBOR_QUALIFIED, "", "Sec. 1259(c)(3)(B)")

    @staticmethod
    def _not_applicable(
        unrealized_gain: float, reason: str, citation: str
    ) -> ConstructiveSaleResult:
        return ConstructiveSaleResult(
            status=STATUS_NOT_APPLICABLE,
            unrealized_gain=round(unrealized_gain, 2),
            realized_taxable_gain=0.0,
            constructive_sale_date=None,
            reason=reason,
            statutory_citation=citation,
        )

    @staticmethod
    def _triggered(
        position: AppreciatedPosition,
        offsetting: OffsettingTransaction,
        unrealized_gain: float,
        gain_at_risk: float,
        offset_quantity: float,
        reason: str,
        citation: str,
    ) -> ConstructiveSaleResult:
        logger.warning(
            "Sec. 1259 constructive sale triggered for %s on %s: %s",
            position.symbol,
            offsetting.entry_date,
            reason,
        )
        return ConstructiveSaleResult(
            status=STATUS_CONSTRUCTIVE_SALE_TRIGGERED,
            unrealized_gain=round(unrealized_gain, 2),
            realized_taxable_gain=round(gain_at_risk, 2),
            # Sec. 1259(a)(1): the constructive sale occurs when the offsetting
            # transaction is entered into.
            constructive_sale_date=offsetting.entry_date,
            reason=reason,
            statutory_citation=citation,
            constructively_sold_quantity=offset_quantity,
            # Sec. 1259(a)(2)(A) and (B).
            adjusted_basis_per_share=round(position.fair_market_value_per_share, 6),
            new_holding_period_start_date=offsetting.entry_date,
        )
