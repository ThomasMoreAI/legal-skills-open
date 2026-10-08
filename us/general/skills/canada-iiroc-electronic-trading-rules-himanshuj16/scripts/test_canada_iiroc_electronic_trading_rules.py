import unittest
from canada_iiroc_electronic_trading_rules import (
    CiroPreTradeRiskEngine,
    ComplianceResult,
    Order,
    OrderMarker,
    OrderSide,
    RegulatoryViolationError,
    RiskLimits,
    ViolationCode,
)


class TestCiroElectronicTradingRules(unittest.TestCase):
    def setUp(self):
        self.limits = RiskLimits(
            max_order_quantity=50000,
            max_order_value_cad=500000.0,
            max_price_deviation_pct=0.10
        )
        self.engine = CiroPreTradeRiskEngine(self.limits)

    def _order(self, **overrides):
        base = dict(
            order_id="ORD",
            symbol="RY.TO",
            side=OrderSide.BUY,
            quantity=1000,
            price=120.0,
            current_inventory=0,
            last_traded_price=121.0,
        )
        base.update(overrides)
        return Order(**base)

    def test_clean_order(self):
        order = Order(
            order_id="ORD1",
            symbol="RY.TO",
            side=OrderSide.BUY,
            quantity=1000,
            price=120.0,
            current_inventory=0,
            last_traded_price=121.0
        )
        res = self.engine.validate_order(order)
        self.assertTrue(res.is_compliant)

    def test_fat_finger_size(self):
        order = Order(
            order_id="ORD2",
            symbol="RY.TO",
            side=OrderSide.BUY,
            quantity=60000,  # Exceeds 50000
            price=1.0,       # Value is only 60k, so value is fine
            current_inventory=0,
            last_traded_price=1.0
        )
        res = self.engine.validate_order(order)
        self.assertFalse(res.is_compliant)
        self.assertIn(ViolationCode.FAT_FINGER_SIZE, res.violations)

    def test_fat_finger_price(self):
        order = Order(
            order_id="ORD3",
            symbol="RY.TO",
            side=OrderSide.BUY,
            quantity=1000,
            price=140.0,     # > 10% deviation from LTP
            current_inventory=0,
            last_traded_price=120.0
        )
        res = self.engine.validate_order(order)
        self.assertFalse(res.is_compliant)
        self.assertIn(ViolationCode.FAT_FINGER_PRICE, res.violations)

    def test_improper_short_mark(self):
        # Selling 1000, but only have 500. Should be marked SELL_SHORT.
        order = Order(
            order_id="ORD4",
            symbol="RY.TO",
            side=OrderSide.SELL,
            quantity=1000,
            price=120.0,
            current_inventory=500,
            last_traded_price=120.0
        )
        res = self.engine.validate_order(order)
        self.assertFalse(res.is_compliant)
        self.assertIn(ViolationCode.IMPROPER_SHORT_MARK, res.violations)

        # Fixing the side flag should pass
        order.side = OrderSide.SELL_SHORT
        res2 = self.engine.validate_order(order)
        self.assertTrue(res2.is_compliant)

    # --- Threshold boundary behaviour -------------------------------------------------

    def test_thresholds_are_inclusive_at_the_exact_limit(self):
        """A value exactly at a configured limit is permitted; only breaches are blocked."""
        order = self._order(quantity=50000, price=10.0, last_traded_price=10.0)
        # 50000 == max_order_quantity, 500_000.0 == max_order_value_cad.
        res = self.engine.validate_order(order)
        self.assertTrue(res.is_compliant, res.reason)

    def test_price_deviation_exactly_at_collar_is_allowed(self):
        # 132.0 is exactly 10% above an LTP of 120.0.
        order = self._order(price=132.0, last_traded_price=120.0)
        self.assertTrue(self.engine.validate_order(order).is_compliant)
        # One cent beyond the collar is rejected.
        order = self._order(price=132.01, last_traded_price=120.0)
        res = self.engine.validate_order(order)
        self.assertFalse(res.is_compliant)
        self.assertIn(ViolationCode.FAT_FINGER_PRICE, res.violations)

    # --- Fail-closed behaviour on unusable inputs -------------------------------------

    def test_missing_reference_price_fails_closed(self):
        """A zero/absent LTP must block the order, not skip the collar check."""
        order = self._order(last_traded_price=0.0)
        res = self.engine.validate_order(order)
        self.assertFalse(res.is_compliant)
        self.assertIn(ViolationCode.REFERENCE_PRICE_UNAVAILABLE, res.violations)

    def test_nan_reference_price_fails_closed(self):
        order = self._order(last_traded_price=float("nan"))
        res = self.engine.validate_order(order)
        self.assertFalse(res.is_compliant)
        self.assertIn(ViolationCode.REFERENCE_PRICE_UNAVAILABLE, res.violations)

    def test_nan_limit_price_is_rejected(self):
        """NaN compares False against every threshold, so it must be caught explicitly."""
        order = self._order(price=float("nan"))
        res = self.engine.validate_order(order)
        self.assertFalse(res.is_compliant)
        self.assertIn(ViolationCode.INVALID_ORDER_PARAMETERS, res.violations)

    def test_infinite_limit_price_is_rejected(self):
        order = self._order(price=float("inf"))
        res = self.engine.validate_order(order)
        self.assertFalse(res.is_compliant)
        self.assertIn(ViolationCode.INVALID_ORDER_PARAMETERS, res.violations)

    def test_non_positive_quantity_is_rejected(self):
        for qty in (0, -100):
            with self.subTest(qty=qty):
                res = self.engine.validate_order(self._order(quantity=qty))
                self.assertFalse(res.is_compliant)
                self.assertIn(ViolationCode.INVALID_ORDER_PARAMETERS, res.violations)

    def test_malformed_field_types_are_rejected_not_coerced(self):
        """Wrong types must not silently fall through into a permissive branch."""
        cases = {
            "bool_quantity": dict(quantity=True),
            "float_quantity": dict(quantity=1000.0),
            "string_side": dict(side="SELL"),
            "string_marker": dict(marker="SHORT"),
            "none_open_notional": dict(open_order_notional_cad=None),
            "nan_open_notional": dict(open_order_notional_cad=float("nan")),
            "none_reference_price": dict(last_traded_price=None),
        }
        for label, overrides in cases.items():
            with self.subTest(label):
                res = self.engine.validate_order(self._order(**overrides))
                self.assertFalse(res.is_compliant)

    def test_negative_limit_price_is_rejected(self):
        res = self.engine.validate_order(self._order(price=-120.0))
        self.assertFalse(res.is_compliant)
        self.assertIn(ViolationCode.INVALID_ORDER_PARAMETERS, res.violations)

    # --- Market orders ----------------------------------------------------------------

    def test_market_order_is_valued_at_reference_price_and_not_collared(self):
        order = self._order(price=None, quantity=1000, last_traded_price=120.0)
        res = self.engine.validate_order(order)
        self.assertTrue(res.is_compliant, res.reason)

    def test_market_order_still_subject_to_notional_cap(self):
        # 5000 x 120.0 = 600,000 > 500,000 cap.
        order = self._order(price=None, quantity=5000, last_traded_price=120.0)
        res = self.engine.validate_order(order)
        self.assertFalse(res.is_compliant)
        self.assertIn(ViolationCode.MAX_CAPITAL_EXCEEDED, res.violations)

    # --- Aggregate unexecuted order value ---------------------------------------------

    def test_aggregate_open_order_value_breach(self):
        engine = CiroPreTradeRiskEngine(RiskLimits(
            max_order_quantity=50000,
            max_order_value_cad=500000.0,
            max_price_deviation_pct=0.10,
            max_open_order_notional_cad=250000.0,
        ))
        # This order alone (1000 x 120 = 120,000) is within the single-order cap, but
        # combined with 200,000 already resting it breaches the aggregate limit.
        order = self._order(price=120.0, last_traded_price=120.0,
                            open_order_notional_cad=200000.0)
        res = engine.validate_order(order)
        self.assertFalse(res.is_compliant)
        self.assertIn(ViolationCode.AGGREGATE_OPEN_ORDER_VALUE_EXCEEDED, res.violations)

    def test_aggregate_control_disabled_by_default(self):
        order = self._order(price=120.0, last_traded_price=120.0,
                            open_order_notional_cad=10_000_000.0)
        self.assertTrue(self.engine.validate_order(order).is_compliant)

    def test_negative_open_order_notional_is_rejected(self):
        res = self.engine.validate_order(self._order(open_order_notional_cad=-1.0))
        self.assertFalse(res.is_compliant)
        self.assertIn(ViolationCode.INVALID_ORDER_PARAMETERS, res.violations)

    # --- UMIR 6.2 designation ---------------------------------------------------------

    def test_covered_sale_marked_short_is_a_misdesignation(self):
        """Over-marking a fully covered sale as short breaches UMIR 6.2 just as under-marking does."""
        order = self._order(side=OrderSide.SELL_SHORT, quantity=1000, current_inventory=1000,
                            price=120.0, last_traded_price=120.0)
        res = self.engine.validate_order(order)
        self.assertFalse(res.is_compliant)
        self.assertIn(ViolationCode.MISMARKED_LONG_SALE, res.violations)

    def test_covered_sale_unmarked_is_compliant(self):
        order = self._order(side=OrderSide.SELL, quantity=1000, current_inventory=1000,
                            price=120.0, last_traded_price=120.0)
        self.assertTrue(self.engine.validate_order(order).is_compliant)

    def test_sme_account_must_mark_every_order_sme(self):
        # A buy from an SME account carrying no designation is non-compliant.
        order = self._order(side=OrderSide.BUY, account_is_short_marking_exempt=True)
        res = self.engine.validate_order(order)
        self.assertFalse(res.is_compliant)
        self.assertIn(ViolationCode.IMPROPER_SME_MARK, res.violations)

        order.marker = OrderMarker.SHORT_MARKING_EXEMPT
        self.assertTrue(self.engine.validate_order(order).is_compliant)

    def test_sme_account_short_sale_must_not_carry_short_marker(self):
        order = self._order(side=OrderSide.SELL_SHORT, quantity=1000, current_inventory=0,
                            price=120.0, last_traded_price=120.0,
                            account_is_short_marking_exempt=True)
        res = self.engine.validate_order(order)
        self.assertFalse(res.is_compliant)
        self.assertIn(ViolationCode.IMPROPER_SME_MARK, res.violations)

        order.marker = OrderMarker.SHORT_MARKING_EXEMPT
        self.assertTrue(self.engine.validate_order(order).is_compliant)

    def test_sme_marker_on_non_exempt_account_is_rejected(self):
        order = self._order(side=OrderSide.SELL, quantity=1000, current_inventory=0,
                            price=120.0, last_traded_price=120.0,
                            marker=OrderMarker.SHORT_MARKING_EXEMPT)
        res = self.engine.validate_order(order)
        self.assertFalse(res.is_compliant)
        self.assertIn(ViolationCode.IMPROPER_SME_MARK, res.violations)

    def test_buy_order_must_not_carry_short_marker(self):
        order = self._order(side=OrderSide.BUY, marker=OrderMarker.SHORT)
        res = self.engine.validate_order(order)
        self.assertFalse(res.is_compliant)
        self.assertIn(ViolationCode.MISMARKED_LONG_SALE, res.violations)

    def test_explicit_marker_overrides_side_inference(self):
        order = self._order(side=OrderSide.SELL, quantity=1000, current_inventory=0,
                            price=120.0, last_traded_price=120.0,
                            marker=OrderMarker.SHORT)
        self.assertTrue(self.engine.validate_order(order).is_compliant)

    # --- Hard gate --------------------------------------------------------------------

    def test_enforce_order_raises_on_violation(self):
        order = self._order(quantity=60000, price=1.0, last_traded_price=1.0)
        with self.assertRaises(RegulatoryViolationError) as ctx:
            self.engine.enforce_order(order)
        self.assertIn(ViolationCode.FAT_FINGER_SIZE, ctx.exception.violations)

    def test_enforce_order_returns_result_when_compliant(self):
        result = self.engine.enforce_order(self._order())
        self.assertIsInstance(result, ComplianceResult)
        self.assertTrue(result.is_compliant)

    def test_result_violations_are_not_shared_between_calls(self):
        first = self.engine.validate_order(self._order(quantity=60000, price=1.0,
                                                       last_traded_price=1.0))
        first.violations.append(ViolationCode.FAT_FINGER_PRICE)
        second = self.engine.validate_order(self._order(quantity=60000, price=1.0,
                                                        last_traded_price=1.0))
        self.assertEqual(second.violations, [ViolationCode.FAT_FINGER_SIZE])


if __name__ == '__main__':
    unittest.main()
