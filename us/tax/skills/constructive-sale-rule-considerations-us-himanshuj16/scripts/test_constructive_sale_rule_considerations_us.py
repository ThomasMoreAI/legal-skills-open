import unittest
from datetime import date

from constructive_sale_rule_considerations_us import (
    AppreciatedPosition,
    ConstructiveSaleError,
    ConstructiveSaleRuleEngine,
    OffsettingTransaction,
    RiskReductionEvent,
)


class TestConstructiveSaleRuleEngine(unittest.TestCase):

    def setUp(self):
        self.engine = ConstructiveSaleRuleEngine()
        # Appreciated position: 1,000 shares, Basis $100/sh ($100k), FMV $250/sh ($250k) -> Gain $150k
        self.appreciated_pos = AppreciatedPosition(
            symbol="NVDA", quantity=1000, cost_basis_per_share=100.0, fair_market_value_per_share=250.0
        )
        # Loss position: 1,000 shares, Basis $200/sh ($200k), FMV $150/sh ($150k) -> Loss -$50k
        self.loss_pos = AppreciatedPosition(
            symbol="BAD_STOCK", quantity=1000, cost_basis_per_share=200.0, fair_market_value_per_share=150.0
        )

    def _short(self, **overrides):
        params = dict(
            transaction_type="SHORT_SALE",
            entry_date=date(2025, 12, 1),
            close_date=date(2026, 1, 15),
            tax_year_end_date=date(2025, 12, 31),
        )
        params.update(overrides)
        return OffsettingTransaction(**params)

    # --- Sec. 1259(b): appreciated financial position gate -----------------

    def test_loss_position_not_applicable(self):
        offsetting = OffsettingTransaction(
            transaction_type="SHORT_SALE",
            entry_date=date(2025, 6, 1),
            close_date=None,
            tax_year_end_date=date(2025, 12, 31),
        )
        res = self.engine.evaluate_transaction(self.loss_pos, offsetting)
        self.assertEqual(res.status, "NOT_APPLICABLE")
        self.assertEqual(res.realized_taxable_gain, 0.0)

    def test_break_even_position_not_applicable(self):
        # Sec. 1259(b)(1) requires that there "would be gain"; exactly zero is not gain.
        flat = AppreciatedPosition(
            symbol="FLAT", quantity=100, cost_basis_per_share=50.0, fair_market_value_per_share=50.0
        )
        res = self.engine.evaluate_transaction(flat, self._short())
        self.assertEqual(res.status, "NOT_APPLICABLE")
        self.assertEqual(res.unrealized_gain, 0.0)

    def test_marked_to_market_position_excluded(self):
        # Sec. 1259(b)(2)(C): a marked-to-market position is not an appreciated
        # financial position, so shorting against it cannot be a constructive sale.
        mtm = AppreciatedPosition(
            symbol="ES_FUT",
            quantity=10,
            cost_basis_per_share=4000.0,
            fair_market_value_per_share=4500.0,
            is_marked_to_market=True,
        )
        res = self.engine.evaluate_transaction(mtm, self._short(close_date=None))
        self.assertEqual(res.status, "NOT_APPLICABLE")
        self.assertEqual(res.realized_taxable_gain, 0.0)
        self.assertIn("1259(b)(2)", res.statutory_citation)

    def test_no_offsetting_transaction(self):
        res = self.engine.evaluate_transaction(self.appreciated_pos, None)
        self.assertEqual(res.status, "NOT_APPLICABLE")
        self.assertEqual(res.unrealized_gain, 150000.0)

    # --- Sec. 1259(c)(1): which transactions are per se constructive sales --

    def test_itm_put_is_not_a_per_se_constructive_sale(self):
        # Sec. 1259(c)(1)(A)-(D) does not list options. An in-the-money put can
        # reach Sec. 1259 only through (c)(1)(E) regulations, which Treasury has
        # never issued -- the engine must escalate, not auto-trigger.
        offsetting = self._short(transaction_type="ITM_PUT", close_date=None)
        res = self.engine.evaluate_transaction(self.appreciated_pos, offsetting)
        self.assertEqual(res.status, "MANUAL_REVIEW_REQUIRED")
        self.assertEqual(res.realized_taxable_gain, 0.0)
        self.assertIsNone(res.constructive_sale_date)
        self.assertIn("1259(c)(1)(E)", res.statutory_citation)

    def test_collar_is_not_a_per_se_constructive_sale(self):
        offsetting = self._short(transaction_type="COLLAR", close_date=None)
        res = self.engine.evaluate_transaction(self.appreciated_pos, offsetting)
        self.assertEqual(res.status, "MANUAL_REVIEW_REQUIRED")

    def test_forward_contract_is_per_se(self):
        # Sec. 1259(c)(1)(C).
        offsetting = self._short(transaction_type="FORWARD_CONTRACT", close_date=None)
        res = self.engine.evaluate_transaction(self.appreciated_pos, offsetting)
        self.assertEqual(res.status, "CONSTRUCTIVE_SALE_TRIGGERED")

    # --- Sec. 1259(c)(3)(A)(i): 30-day close deadline ----------------------

    def test_safe_harbor_qualified(self):
        # Entry Dec 1, 2025. Closed Jan 15, 2026 (before the Jan 30 deadline).
        # Held unhedged 60+ days.
        offsetting = self._short(re_hedged_during_60_days=False)
        res = self.engine.evaluate_transaction(self.appreciated_pos, offsetting)
        self.assertEqual(res.status, "SAFE_HARBOR_QUALIFIED")
        self.assertEqual(res.realized_taxable_gain, 0.0)
        self.assertIsNone(res.adjusted_basis_per_share)

    def test_close_exactly_on_thirtieth_day_qualifies(self):
        # 30th day after Dec 31, 2025 is Jan 30, 2026 -- "on or before" includes it.
        res = self.engine.evaluate_transaction(
            self.appreciated_pos, self._short(close_date=date(2026, 1, 30))
        )
        self.assertEqual(res.status, "SAFE_HARBOR_QUALIFIED")

    def test_close_one_day_late_fails(self):
        res = self.engine.evaluate_transaction(
            self.appreciated_pos, self._short(close_date=date(2026, 1, 31))
        )
        self.assertEqual(res.status, "CONSTRUCTIVE_SALE_TRIGGERED")
        self.assertEqual(res.realized_taxable_gain, 150000.0)

    def test_non_calendar_fiscal_year_end(self):
        # A June 30 fiscal year end moves the deadline to July 30, not Jan 30.
        offsetting = OffsettingTransaction(
            transaction_type="SHORT_SALE",
            entry_date=date(2025, 5, 1),
            close_date=date(2025, 7, 29),
            tax_year_end_date=date(2025, 6, 30),
        )
        res = self.engine.evaluate_transaction(self.appreciated_pos, offsetting)
        self.assertEqual(res.status, "SAFE_HARBOR_QUALIFIED")

        late = OffsettingTransaction(
            transaction_type="SHORT_SALE",
            entry_date=date(2025, 5, 1),
            close_date=date(2025, 8, 1),
            tax_year_end_date=date(2025, 6, 30),
        )
        self.assertEqual(
            self.engine.evaluate_transaction(self.appreciated_pos, late).status,
            "CONSTRUCTIVE_SALE_TRIGGERED",
        )

    def test_late_close_triggers_constructive_sale(self):
        # Closed Feb 15, 2026 (past the Jan 30 deadline) -> constructive sale on entry date.
        offsetting = self._short(close_date=date(2026, 2, 15))
        res = self.engine.evaluate_transaction(self.appreciated_pos, offsetting)
        self.assertEqual(res.status, "CONSTRUCTIVE_SALE_TRIGGERED")
        self.assertEqual(res.realized_taxable_gain, 150000.0)  # $250k - $100k
        self.assertEqual(res.constructive_sale_date, date(2025, 12, 1))

    def test_never_closed_triggers_constructive_sale(self):
        res = self.engine.evaluate_transaction(self.appreciated_pos, self._short(close_date=None))
        self.assertEqual(res.status, "CONSTRUCTIVE_SALE_TRIGGERED")
        self.assertEqual(res.constructive_sale_date, date(2025, 12, 1))

    # --- Sec. 1259(a)(2): basis and holding period consequences ------------

    def test_constructive_sale_reports_basis_and_holding_period(self):
        res = self.engine.evaluate_transaction(
            self.appreciated_pos, self._short(close_date=date(2026, 2, 15))
        )
        # Sec. 1259(a)(2): new basis = FMV recognized; holding period restarts.
        self.assertEqual(res.adjusted_basis_per_share, 250.0)
        self.assertEqual(res.new_holding_period_start_date, date(2025, 12, 1))
        self.assertEqual(res.constructively_sold_quantity, 1000)

    # --- Partial hedges ----------------------------------------------------

    def test_partial_hedge_recognizes_only_hedged_portion(self):
        # 400 of 1,000 shares shorted -> 40% of the $150k gain = $60k.
        offsetting = self._short(close_date=date(2026, 2, 15), offsetting_quantity=400)
        res = self.engine.evaluate_transaction(self.appreciated_pos, offsetting)
        self.assertEqual(res.status, "CONSTRUCTIVE_SALE_TRIGGERED")
        self.assertEqual(res.unrealized_gain, 150000.0)
        self.assertEqual(res.realized_taxable_gain, 60000.0)
        self.assertEqual(res.constructively_sold_quantity, 400)

    def test_over_hedge_capped_at_position_quantity(self):
        offsetting = self._short(close_date=date(2026, 2, 15), offsetting_quantity=5000)
        res = self.engine.evaluate_transaction(self.appreciated_pos, offsetting)
        self.assertEqual(res.realized_taxable_gain, 150000.0)
        self.assertEqual(res.constructively_sold_quantity, 1000)

    # --- Sec. 1259(c)(3)(A)(ii): must hold the position 60 days ------------

    def test_disposal_inside_60_day_window_fails_safe_harbor(self):
        # Closed Jan 15, 2026 -> window runs Jan 15 through Mar 15, 2026.
        offsetting = self._short(long_position_disposal_date=date(2026, 2, 20))
        res = self.engine.evaluate_transaction(self.appreciated_pos, offsetting)
        self.assertEqual(res.status, "CONSTRUCTIVE_SALE_TRIGGERED")
        self.assertEqual(res.realized_taxable_gain, 150000.0)
        self.assertIn("1259(c)(3)(A)(ii)", res.statutory_citation)

    def test_disposal_on_last_day_of_window_fails(self):
        # Day 60 of a period beginning Jan 15, 2026 is Mar 15, 2026.
        offsetting = self._short(long_position_disposal_date=date(2026, 3, 15))
        self.assertEqual(
            self.engine.evaluate_transaction(self.appreciated_pos, offsetting).status,
            "CONSTRUCTIVE_SALE_TRIGGERED",
        )

    def test_disposal_after_window_is_fine(self):
        offsetting = self._short(long_position_disposal_date=date(2026, 3, 16))
        self.assertEqual(
            self.engine.evaluate_transaction(self.appreciated_pos, offsetting).status,
            "SAFE_HARBOR_QUALIFIED",
        )

    # --- Sec. 1259(c)(3)(A)(iii) and (c)(3)(B): risk-of-loss reduction -----

    def test_rehedged_in_60_days_triggers_constructive_sale(self):
        # Closed Jan 10, 2026, but re-hedged inside the 60-day window with no
        # evidence of Sec. 1259(c)(3)(B) relief -> constructive sale.
        offsetting = OffsettingTransaction(
            transaction_type="EQUITY_SWAP",
            entry_date=date(2025, 11, 1),
            close_date=date(2026, 1, 10),
            tax_year_end_date=date(2025, 12, 31),
            re_hedged_during_60_days=True,
        )
        res = self.engine.evaluate_transaction(self.appreciated_pos, offsetting)
        self.assertEqual(res.status, "CONSTRUCTIVE_SALE_TRIGGERED")
        self.assertEqual(res.realized_taxable_gain, 150000.0)

    def test_protective_put_in_window_left_open_fails(self):
        # Sec. 246(c)(4)(A): holding an option to sell reduces risk of loss.
        offsetting = self._short(
            risk_reduction_events=[
                RiskReductionEvent(
                    event_type="PROTECTIVE_PUT",
                    start_date=date(2026, 2, 1),
                    close_date=None,
                )
            ]
        )
        res = self.engine.evaluate_transaction(self.appreciated_pos, offsetting)
        self.assertEqual(res.status, "CONSTRUCTIVE_SALE_TRIGGERED")
        self.assertIn("1259(c)(3)(A)(iii)", res.statutory_citation)

    def test_risk_reduction_outside_window_is_ignored(self):
        # Window is Jan 15 - Mar 15, 2026; a hedge opened Apr 1 is irrelevant.
        offsetting = self._short(
            risk_reduction_events=[
                RiskReductionEvent(
                    event_type="PROTECTIVE_PUT", start_date=date(2026, 4, 1), close_date=None
                )
            ]
        )
        self.assertEqual(
            self.engine.evaluate_transaction(self.appreciated_pos, offsetting).status,
            "SAFE_HARBOR_QUALIFIED",
        )

    def test_second_transaction_disregarded_under_c3B(self):
        # Original short closed Jan 5, 2026 (deadline Jan 30, 2026). A second
        # hedge opens Jan 10 and is itself closed Jan 20 -- before the same
        # deadline -- with a clean 60 days after it. Sec. 1259(c)(3)(B) then
        # disregards the second transaction, preserving the safe harbor.
        offsetting = self._short(
            close_date=date(2026, 1, 5),
            risk_reduction_events=[
                RiskReductionEvent(
                    event_type="SHORT_SALE",
                    start_date=date(2026, 1, 10),
                    close_date=date(2026, 1, 20),
                )
            ],
        )
        res = self.engine.evaluate_transaction(self.appreciated_pos, offsetting)
        self.assertEqual(res.status, "SAFE_HARBOR_QUALIFIED")
        self.assertEqual(res.realized_taxable_gain, 0.0)

    def test_second_transaction_closed_after_deadline_is_not_disregarded(self):
        # Same shape, but the second hedge closes Feb 10, 2026 -- past the
        # Jan 30 deadline required by Sec. 1259(c)(3)(B)(ii)(II).
        offsetting = self._short(
            close_date=date(2026, 1, 5),
            risk_reduction_events=[
                RiskReductionEvent(
                    event_type="SHORT_SALE",
                    start_date=date(2026, 1, 10),
                    close_date=date(2026, 2, 10),
                )
            ],
        )
        res = self.engine.evaluate_transaction(self.appreciated_pos, offsetting)
        self.assertEqual(res.status, "CONSTRUCTIVE_SALE_TRIGGERED")
        self.assertEqual(res.constructive_sale_date, date(2025, 12, 1))

    def test_second_transaction_with_disposal_in_its_own_window_fails(self):
        # The first window ends Mar 5, 2026, so a Mar 10 disposal clears
        # Sec. 1259(c)(3)(A)(ii). But the second transaction closed Jan 20, so
        # its own 60-day period runs to Mar 20 -- the disposal lands inside it
        # and Sec. 1259(c)(3)(B)(ii)(III) denies the carve-out.
        offsetting = self._short(
            close_date=date(2026, 1, 5),
            long_position_disposal_date=date(2026, 3, 10),
            risk_reduction_events=[
                RiskReductionEvent(
                    event_type="SHORT_SALE",
                    start_date=date(2026, 1, 10),
                    close_date=date(2026, 1, 20),
                )
            ],
        )
        res = self.engine.evaluate_transaction(self.appreciated_pos, offsetting)
        self.assertEqual(res.status, "CONSTRUCTIVE_SALE_TRIGGERED")

    def test_chained_risk_reductions_escalate_for_review(self):
        # A third hedge inside the second one's 60-day period. The statute does
        # not clearly allow chained (c)(3)(B) relief, so escalate.
        offsetting = self._short(
            close_date=date(2026, 1, 5),
            risk_reduction_events=[
                RiskReductionEvent(
                    event_type="SHORT_SALE",
                    start_date=date(2026, 1, 10),
                    close_date=date(2026, 1, 20),
                ),
                RiskReductionEvent(
                    event_type="PROTECTIVE_PUT",
                    start_date=date(2026, 1, 25),
                    close_date=date(2026, 1, 28),
                ),
            ],
        )
        res = self.engine.evaluate_transaction(self.appreciated_pos, offsetting)
        self.assertEqual(res.status, "MANUAL_REVIEW_REQUIRED")
        self.assertEqual(res.realized_taxable_gain, 0.0)

    # --- Input validation --------------------------------------------------

    def test_close_before_entry_rejected(self):
        with self.assertRaises(ConstructiveSaleError):
            self.engine.evaluate_transaction(
                self.appreciated_pos,
                self._short(entry_date=date(2025, 12, 1), close_date=date(2025, 11, 1)),
            )

    def test_tax_year_end_before_entry_rejected(self):
        # Sec. 1259(c)(3)(A)(i) measures from the year end of the year the
        # transaction was entered into; a prior year end is a config error.
        with self.assertRaises(ConstructiveSaleError):
            self.engine.evaluate_transaction(
                self.appreciated_pos,
                self._short(entry_date=date(2026, 1, 5), tax_year_end_date=date(2025, 12, 31)),
            )

    def test_tax_year_end_more_than_a_year_after_entry_rejected(self):
        with self.assertRaises(ConstructiveSaleError):
            self.engine.evaluate_transaction(
                self.appreciated_pos,
                self._short(entry_date=date(2024, 1, 1), tax_year_end_date=date(2025, 12, 31)),
            )

    def test_non_positive_quantity_rejected(self):
        bad = AppreciatedPosition(
            symbol="X", quantity=0, cost_basis_per_share=10.0, fair_market_value_per_share=20.0
        )
        with self.assertRaises(ConstructiveSaleError):
            self.engine.evaluate_transaction(bad, self._short())

    def test_nan_fmv_rejected(self):
        bad = AppreciatedPosition(
            symbol="X",
            quantity=100,
            cost_basis_per_share=10.0,
            fair_market_value_per_share=float("nan"),
        )
        with self.assertRaises(ConstructiveSaleError):
            self.engine.evaluate_transaction(bad, self._short())

    def test_valuation_date_must_match_constructive_sale_date(self):
        # Sec. 1259(a)(1) measures gain at the constructive sale date, so a
        # today-dated FMV must be rejected rather than silently used.
        mis_dated = AppreciatedPosition(
            symbol="NVDA",
            quantity=1000,
            cost_basis_per_share=100.0,
            fair_market_value_per_share=250.0,
            valuation_date=date(2026, 6, 1),
        )
        with self.assertRaises(ConstructiveSaleError):
            self.engine.evaluate_transaction(mis_dated, self._short())

    def test_mis_dated_fmv_rejected_even_when_it_looks_like_a_loss(self):
        # A price taken on the wrong date can make an appreciated position look
        # like a loss; the date check must fire before the Sec. 1259(b)(1) gate
        # rather than silently returning NOT_APPLICABLE.
        mis_dated_loss = AppreciatedPosition(
            symbol="NVDA",
            quantity=1000,
            cost_basis_per_share=100.0,
            fair_market_value_per_share=80.0,
            valuation_date=date(2026, 6, 1),
        )
        with self.assertRaises(ConstructiveSaleError):
            self.engine.evaluate_transaction(mis_dated_loss, self._short())

    def test_matching_valuation_date_accepted(self):
        priced = AppreciatedPosition(
            symbol="NVDA",
            quantity=1000,
            cost_basis_per_share=100.0,
            fair_market_value_per_share=250.0,
            valuation_date=date(2025, 12, 1),
        )
        res = self.engine.evaluate_transaction(priced, self._short(close_date=date(2026, 2, 15)))
        self.assertEqual(res.status, "CONSTRUCTIVE_SALE_TRIGGERED")
        self.assertEqual(res.realized_taxable_gain, 150000.0)


if __name__ == '__main__':
    unittest.main()
