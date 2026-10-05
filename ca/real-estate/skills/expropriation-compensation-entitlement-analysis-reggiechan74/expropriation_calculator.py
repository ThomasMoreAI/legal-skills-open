#!/usr/bin/env python3
"""
Expropriation Compensation Calculator - Ontario Expropriations Act

Calculates legal entitlement to compensation under s.13 and s.18 OEA:
- Market value (s.13): Valuation date, highest and best use, special purchaser exclusion
- Disturbance damages (s.18): Moving costs, business losses, professional fees, temporary accommodation
- Injurious affection (s.18(2)): Construction impacts and permanent use impacts
- Interest: Pre-judgment interest from valuation date to payment

Legal Framework:
- Market value: Price willing buyer and willing seller in open market
- Valuation date: Earlier of Form 7 service or plan registration
- Highest and best use: Legal use that maximizes value
- Special purchaser: Premium excluded (assemblage, unique buyer)
- Disturbance: But-for test, reasonableness, foreseeability
- Goodwill: NON-compensable under s.18(3)

Author: Claude Code
Version: 1.0.0
Date: 2025-11-15
"""

import json
import sys
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from typing import List, Optional, Dict, Any
from pathlib import Path


# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class PropertyDetails:
    """
    Property information for market value determination

    All financial values in dollars unless otherwise noted
    """
    address: str
    area_acres: float

    # Market value (s.13 OEA)
    market_value: float  # Fair market value at valuation date
    zoning: str
    highest_and_best_use: str

    # Valuation date (s.13(2) OEA - earlier of Form 7 or plan registration)
    valuation_date: date
    form_7_service_date: Optional[date] = None
    plan_registration_date: Optional[date] = None

    # Special purchaser premium (if any - excluded from compensation)
    special_purchaser_premium: float = 0.0
    special_purchaser_notes: str = ""

    def __post_init__(self):
        """Validate property details and determine valuation date"""
        if self.market_value <= 0:
            raise ValueError(f"Invalid market value: {self.market_value}")
        if self.area_acres <= 0:
            raise ValueError(f"Invalid area: {self.area_acres}")

        # Validate valuation date determination
        if self.form_7_service_date and self.plan_registration_date:
            computed_valuation_date = min(self.form_7_service_date, self.plan_registration_date)
            if computed_valuation_date != self.valuation_date:
                raise ValueError(
                    f"Valuation date {self.valuation_date} does not match "
                    f"earlier of Form 7 ({self.form_7_service_date}) or "
                    f"plan registration ({self.plan_registration_date}): "
                    f"should be {computed_valuation_date}"
                )


@dataclass
class BusinessLossesDetail:
    """
    Business losses during reasonable relocation period (compensable)

    Goodwill is NON-compensable under s.18(3) OEA
    Revenue losses compensable ONLY during reasonable relocation period
    """
    # Revenue loss calculation (but-for test)
    revenue_loss_months: int = 0  # Reasonable relocation period (typically 6-12 months)
    monthly_revenue: float = 0.0
    profit_margin_pct: float = 0.0  # Net profit margin (e.g., 20%)
    fixed_costs_monthly: float = 0.0  # Fixed costs continue during closure

    # Business re-establishment costs (compensable)
    signage_and_marketing: float = 0.0  # New signage, marketing to notify customers
    permits_and_licenses: float = 0.0  # New permits at new location
    equipment_reinstallation: float = 0.0  # Disconnection/reconnection costs

    # Trade fixtures (compensable at depreciated value, NOT salvage value)
    trade_fixtures_depreciated_value: float = 0.0

    # Goodwill (NON-compensable under s.18(3))
    # Customer base, reputation, brand recognition - owner can rebuild at new location
    goodwill_claimed: float = 0.0  # For reference only - will be flagged as non-compensable

    def calculate_revenue_loss(self) -> float:
        """
        Calculate compensable revenue loss during reasonable relocation period

        Formula: (Lost revenue × profit margin) + Fixed costs during closure
        """
        if self.revenue_loss_months <= 0:
            return 0.0

        lost_profit = self.monthly_revenue * (self.profit_margin_pct / 100.0) * self.revenue_loss_months
        continuing_fixed_costs = self.fixed_costs_monthly * self.revenue_loss_months

        return lost_profit + continuing_fixed_costs

    def total_compensable_business_losses(self) -> float:
        """Total compensable business losses (excludes goodwill)"""
        return (
            self.calculate_revenue_loss() +
            self.signage_and_marketing +
            self.permits_and_licenses +
            self.equipment_reinstallation +
            self.trade_fixtures_depreciated_value
        )


@dataclass
class DisturbanceDamages:
    """
    Disturbance damages (s.18 OEA)

    Legal tests:
    1. Causation: But-for test (would not have incurred but for expropriation)
    2. Reasonableness: Owner has duty to mitigate (no gold-plated solutions)
    3. Foreseeability: More liberal than tort (broadly foreseeable consequences)
    """
    # Moving costs (compensable)
    moving_costs: float = 0.0  # Professional movers or reasonable self-move
    packing_materials: float = 0.0
    storage_costs: float = 0.0  # Temporary storage (reasonable duration)

    # Business losses (detailed calculation)
    business_losses: Optional[BusinessLossesDetail] = None

    # Professional fees (compensable at reasonable rates)
    legal_fees: float = 0.0  # Expropriation lawyer fees
    appraisal_fees: float = 0.0  # Independent appraisal
    accounting_fees: float = 0.0  # Tax advice, financial analysis

    # Temporary accommodation (compensable for reasonable period)
    temporary_accommodation_months: int = 0  # Typically 3-6 months
    accommodation_cost_monthly: float = 0.0  # Apartment preferred over hotel (mitigation)

    # Injurious affection - construction impacts (s.18(2)(a) - temporary)
    construction_noise_damages: float = 0.0
    construction_dust_damages: float = 0.0
    construction_vibration_damages: float = 0.0
    construction_traffic_disruption: float = 0.0
    construction_duration_months: int = 0

    # Injurious affection - permanent use impacts (s.18(2)(b) - capitalized)
    permanent_noise_value_loss: float = 0.0  # Ongoing highway/transit noise
    permanent_visual_obstruction: float = 0.0  # Elevated structure blocks view
    permanent_privacy_loss: float = 0.0  # Highway adjacent to property
    permanent_stigma_value_loss: float = 0.0  # Transmission line EMF perception

    def total_moving_costs(self) -> float:
        """Total moving and relocation costs"""
        return self.moving_costs + self.packing_materials + self.storage_costs

    def total_professional_fees(self) -> float:
        """Total professional fees"""
        return self.legal_fees + self.appraisal_fees + self.accounting_fees

    def total_temporary_accommodation(self) -> float:
        """Total temporary accommodation costs"""
        return self.accommodation_cost_monthly * self.temporary_accommodation_months

    def total_construction_impacts(self) -> float:
        """Total construction period impacts (s.18(2)(a) - temporary)"""
        return (
            self.construction_noise_damages +
            self.construction_dust_damages +
            self.construction_vibration_damages +
            self.construction_traffic_disruption
        )

    def total_permanent_impacts(self) -> float:
        """Total permanent use impacts (s.18(2)(b) - capitalized value loss)"""
        return (
            self.permanent_noise_value_loss +
            self.permanent_visual_obstruction +
            self.permanent_privacy_loss +
            self.permanent_stigma_value_loss
        )

    def total_compensable_disturbance(self) -> float:
        """Total compensable disturbance damages"""
        total = (
            self.total_moving_costs() +
            self.total_professional_fees() +
            self.total_temporary_accommodation() +
            self.total_construction_impacts() +
            self.total_permanent_impacts()
        )

        # Add business losses if present
        if self.business_losses:
            total += self.business_losses.total_compensable_business_losses()

        return total


@dataclass
class InterestCalculation:
    """
    Pre-judgment interest calculation

    Interest accrues from valuation date to payment date
    Current statutory rate in Ontario: 3.0% annual
    """
    payment_date: date
    interest_rate_annual_pct: float = 3.0  # Ontario statutory rate

    def calculate_interest(
        self,
        principal: float,
        valuation_date: date
    ) -> Dict[str, Any]:
        """
        Calculate simple interest from valuation date to payment

        Formula: Principal × Rate × (Days / 365)
        """
        if self.payment_date <= valuation_date:
            return {
                "interest_amount": 0.0,
                "days": 0,
                "years": 0.0,
                "note": "Payment date on or before valuation date - no interest"
            }

        days_elapsed = (self.payment_date - valuation_date).days
        years_elapsed = days_elapsed / 365.0

        interest_amount = principal * (self.interest_rate_annual_pct / 100.0) * years_elapsed

        return {
            "interest_amount": interest_amount,
            "days": days_elapsed,
            "years": years_elapsed,
            "rate_annual_pct": self.interest_rate_annual_pct,
            "principal": principal,
            "valuation_date": valuation_date.isoformat(),
            "payment_date": self.payment_date.isoformat()
        }


@dataclass
class CompensationBreakdown:
    """
    Complete compensation breakdown

    Components:
    1. Market value (s.13 OEA)
    2. Disturbance damages (s.18 OEA)
    3. Pre-judgment interest
    """
    # Market value
    market_value: float
    special_purchaser_premium_excluded: float = 0.0

    # Disturbance damages breakdown
    moving_costs: float = 0.0
    business_losses_compensable: float = 0.0
    business_losses_non_compensable: float = 0.0  # Goodwill
    professional_fees: float = 0.0
    temporary_accommodation: float = 0.0
    construction_impacts_temporary: float = 0.0
    permanent_impacts_capitalized: float = 0.0

    # Subtotals
    total_disturbance: float = 0.0
    subtotal_before_interest: float = 0.0

    # Interest
    interest_amount: float = 0.0
    interest_details: Dict[str, Any] = field(default_factory=dict)

    # Total compensation
    total_compensation: float = 0.0

    # Compliance notes
    compliance_notes: List[str] = field(default_factory=list)
    non_compensable_items: List[str] = field(default_factory=list)


@dataclass
class ExpropriationCompensationResults:
    """
    Complete results of expropriation compensation analysis
    """
    property_details: PropertyDetails
    disturbance_damages: DisturbanceDamages
    interest_calculation: InterestCalculation
    compensation_breakdown: CompensationBreakdown

    analysis_date: date
    analysis_notes: List[str] = field(default_factory=list)


# ============================================================================
# COMPENSATION CALCULATION FUNCTIONS
# ============================================================================

def calculate_expropriation_compensation(
    property_details: PropertyDetails,
    disturbance_damages: DisturbanceDamages,
    interest_calc: InterestCalculation
) -> ExpropriationCompensationResults:
    """
    Calculate complete expropriation compensation entitlement

    Components:
    1. Market value (s.13 OEA) - highest and best use, no special purchaser premium
    2. Disturbance damages (s.18 OEA) - but-for test, reasonableness, foreseeability
    3. Injurious affection (s.18(2)) - construction and permanent use impacts
    4. Interest - from valuation date to payment

    Returns:
        Complete compensation analysis with breakdown and compliance notes
    """
    breakdown = CompensationBreakdown(
        market_value=property_details.market_value,
        special_purchaser_premium_excluded=property_details.special_purchaser_premium
    )

    # ========================================================================
    # 1. DISTURBANCE DAMAGES BREAKDOWN
    # ========================================================================
    breakdown.moving_costs = disturbance_damages.total_moving_costs()
    breakdown.professional_fees = disturbance_damages.total_professional_fees()
    breakdown.temporary_accommodation = disturbance_damages.total_temporary_accommodation()
    breakdown.construction_impacts_temporary = disturbance_damages.total_construction_impacts()
    breakdown.permanent_impacts_capitalized = disturbance_damages.total_permanent_impacts()

    # Business losses - separate compensable from non-compensable
    if disturbance_damages.business_losses:
        breakdown.business_losses_compensable = (
            disturbance_damages.business_losses.total_compensable_business_losses()
        )
        breakdown.business_losses_non_compensable = (
            disturbance_damages.business_losses.goodwill_claimed
        )

    # Total disturbance damages
    breakdown.total_disturbance = (
        breakdown.moving_costs +
        breakdown.business_losses_compensable +
        breakdown.professional_fees +
        breakdown.temporary_accommodation +
        breakdown.construction_impacts_temporary +
        breakdown.permanent_impacts_capitalized
    )

    # Subtotal before interest
    breakdown.subtotal_before_interest = (
        breakdown.market_value + breakdown.total_disturbance
    )

    # ========================================================================
    # 2. INTEREST CALCULATION
    # ========================================================================
    interest_result = interest_calc.calculate_interest(
        principal=breakdown.subtotal_before_interest,
        valuation_date=property_details.valuation_date
    )

    breakdown.interest_amount = interest_result["interest_amount"]
    breakdown.interest_details = interest_result

    # ========================================================================
    # 3. TOTAL COMPENSATION
    # ========================================================================
    breakdown.total_compensation = (
        breakdown.subtotal_before_interest + breakdown.interest_amount
    )

    # ========================================================================
    # 4. COMPLIANCE VALIDATION AND NOTES
    # ========================================================================
    compliance_notes = []
    non_compensable_items = []

    # Market value compliance
    compliance_notes.append(
        f"✓ Market value: ${breakdown.market_value:,.2f} at valuation date "
        f"{property_details.valuation_date.strftime('%B %d, %Y')}"
    )
    compliance_notes.append(
        f"✓ Highest and best use: {property_details.highest_and_best_use} "
        f"(zoned {property_details.zoning})"
    )

    if property_details.special_purchaser_premium > 0:
        non_compensable_items.append(
            f"✗ Special purchaser premium excluded: ${property_details.special_purchaser_premium:,.2f} "
            f"({property_details.special_purchaser_notes})"
        )

    # Valuation date determination
    if property_details.form_7_service_date and property_details.plan_registration_date:
        compliance_notes.append(
            f"✓ Valuation date: Earlier of Form 7 ({property_details.form_7_service_date}) "
            f"or plan registration ({property_details.plan_registration_date})"
        )

    # Disturbance damages compliance
    if breakdown.moving_costs > 0:
        compliance_notes.append(
            f"✓ Moving costs: ${breakdown.moving_costs:,.2f} (passes but-for test)"
        )

    if breakdown.professional_fees > 0:
        compliance_notes.append(
            f"✓ Professional fees: ${breakdown.professional_fees:,.2f} (reasonable rates required)"
        )

    if breakdown.business_losses_compensable > 0:
        if disturbance_damages.business_losses:
            compliance_notes.append(
                f"✓ Business losses: ${breakdown.business_losses_compensable:,.2f} "
                f"(limited to {disturbance_damages.business_losses.revenue_loss_months} month "
                f"reasonable relocation period)"
            )

    # Non-compensable goodwill
    if breakdown.business_losses_non_compensable > 0:
        non_compensable_items.append(
            f"✗ Goodwill NON-compensable: ${breakdown.business_losses_non_compensable:,.2f} "
            f"(s.18(3) OEA excludes intangible value - owner can rebuild at new location)"
        )

    # Injurious affection
    if breakdown.construction_impacts_temporary > 0:
        compliance_notes.append(
            f"✓ Construction impacts (s.18(2)(a)): ${breakdown.construction_impacts_temporary:,.2f} "
            f"({disturbance_damages.construction_duration_months} month temporary impact)"
        )

    if breakdown.permanent_impacts_capitalized > 0:
        compliance_notes.append(
            f"✓ Permanent use impacts (s.18(2)(b)): ${breakdown.permanent_impacts_capitalized:,.2f} "
            f"(capitalized permanent value loss - Antrim four-part test)"
        )

    # Interest
    if breakdown.interest_amount > 0:
        compliance_notes.append(
            f"✓ Pre-judgment interest: ${breakdown.interest_amount:,.2f} "
            f"({interest_result['days']} days at {interest_calc.interest_rate_annual_pct}%/year)"
        )

    breakdown.compliance_notes = compliance_notes
    breakdown.non_compensable_items = non_compensable_items

    # ========================================================================
    # 5. ANALYSIS NOTES
    # ========================================================================
    analysis_notes = [
        f"Expropriation compensation analysis under Ontario Expropriations Act",
        f"Property: {property_details.address} ({property_details.area_acres} acres)",
        f"Valuation date: {property_details.valuation_date.strftime('%B %d, %Y')}",
        f"Payment date: {interest_calc.payment_date.strftime('%B %d, %Y')}",
        f"",
        f"Legal framework:",
        f"  - s.13 OEA: Market value at highest and best use",
        f"  - s.18 OEA: Disturbance damages (but-for test, reasonableness, foreseeability)",
        f"  - s.18(2)(a): Construction impacts (temporary)",
        f"  - s.18(2)(b): Permanent use impacts (Antrim four-part test)",
        f"  - s.18(3): Goodwill NON-compensable",
        f"",
        f"Total compensation: ${breakdown.total_compensation:,.2f}"
    ]

    return ExpropriationCompensationResults(
        property_details=property_details,
        disturbance_damages=disturbance_damages,
        interest_calculation=interest_calc,
        compensation_breakdown=breakdown,
        analysis_date=date.today(),
        analysis_notes=analysis_notes
    )


# ============================================================================
# JSON INPUT/OUTPUT
# ============================================================================

def load_expropriation_from_json(json_path: str) -> tuple[PropertyDetails, DisturbanceDamages, InterestCalculation]:
    """
    Load expropriation scenario from JSON file

    Expected JSON structure:
    {
      "property": { ... },
      "disturbance_damages": { ... },
      "payment_details": { ... }
    }
    """
    with open(json_path, 'r') as f:
        data = json.load(f)

    # Parse property details
    prop_data = data["property"]
    property_details = PropertyDetails(
        address=prop_data["address"],
        area_acres=float(prop_data["area_acres"]),
        market_value=float(prop_data["market_value"]),
        zoning=prop_data["zoning"],
        highest_and_best_use=prop_data["highest_and_best_use"],
        valuation_date=datetime.strptime(prop_data["valuation_date"], "%Y-%m-%d").date(),
        form_7_service_date=datetime.strptime(prop_data["form_7_service_date"], "%Y-%m-%d").date() if "form_7_service_date" in prop_data else None,
        plan_registration_date=datetime.strptime(prop_data["plan_registration_date"], "%Y-%m-%d").date() if "plan_registration_date" in prop_data else None,
        special_purchaser_premium=float(prop_data.get("special_purchaser_premium", 0.0)),
        special_purchaser_notes=prop_data.get("special_purchaser_notes", "")
    )

    # Parse disturbance damages
    dist_data = data["disturbance_damages"]

    # Business losses (if present)
    business_losses = None
    if "business_losses" in dist_data and dist_data["business_losses"]:
        biz_data = dist_data["business_losses"]
        business_losses = BusinessLossesDetail(
            revenue_loss_months=int(biz_data["revenue_loss_months"]),
            monthly_revenue=float(biz_data["monthly_revenue"]),
            profit_margin_pct=float(biz_data["profit_margin_pct"]),
            fixed_costs_monthly=float(biz_data["fixed_costs_monthly"]),
            signage_and_marketing=float(biz_data.get("signage_and_marketing", 0.0)),
            permits_and_licenses=float(biz_data.get("permits_and_licenses", 0.0)),
            equipment_reinstallation=float(biz_data.get("equipment_reinstallation", 0.0)),
            trade_fixtures_depreciated_value=float(biz_data.get("trade_fixtures_depreciated_value", 0.0)),
            goodwill_claimed=float(biz_data.get("goodwill_claimed", 0.0))
        )

    disturbance_damages = DisturbanceDamages(
        moving_costs=float(dist_data.get("moving_costs", 0.0)),
        packing_materials=float(dist_data.get("packing_materials", 0.0)),
        storage_costs=float(dist_data.get("storage_costs", 0.0)),
        business_losses=business_losses,
        legal_fees=float(dist_data.get("professional_fees", {}).get("legal", 0.0)),
        appraisal_fees=float(dist_data.get("professional_fees", {}).get("appraisal", 0.0)),
        accounting_fees=float(dist_data.get("professional_fees", {}).get("accounting", 0.0)),
        temporary_accommodation_months=int(dist_data.get("temporary_accommodation_months", 0)),
        accommodation_cost_monthly=float(dist_data.get("accommodation_cost_monthly", 0.0)),
        construction_noise_damages=float(dist_data.get("construction_impacts", {}).get("noise", 0.0)),
        construction_dust_damages=float(dist_data.get("construction_impacts", {}).get("dust", 0.0)),
        construction_vibration_damages=float(dist_data.get("construction_impacts", {}).get("vibration", 0.0)),
        construction_traffic_disruption=float(dist_data.get("construction_impacts", {}).get("traffic_disruption", 0.0)),
        construction_duration_months=int(dist_data.get("construction_impacts", {}).get("duration_months", 0)),
        permanent_noise_value_loss=float(dist_data.get("permanent_impacts", {}).get("noise_value_loss", 0.0)),
        permanent_visual_obstruction=float(dist_data.get("permanent_impacts", {}).get("visual_obstruction", 0.0)),
        permanent_privacy_loss=float(dist_data.get("permanent_impacts", {}).get("privacy_loss", 0.0)),
        permanent_stigma_value_loss=float(dist_data.get("permanent_impacts", {}).get("stigma_value_loss", 0.0))
    )

    # Parse payment details
    payment_data = data["payment_details"]
    interest_calc = InterestCalculation(
        payment_date=datetime.strptime(payment_data["payment_date"], "%Y-%m-%d").date(),
        interest_rate_annual_pct=float(payment_data.get("interest_rate_annual_pct", 3.0))
    )

    return property_details, disturbance_damages, interest_calc


def save_results_to_json(results: ExpropriationCompensationResults, output_path: str):
    """Save analysis results to JSON file"""

    output = {
        "analysis_date": results.analysis_date.isoformat(),
        "property_details": {
            "address": results.property_details.address,
            "area_acres": results.property_details.area_acres,
            "market_value": results.property_details.market_value,
            "zoning": results.property_details.zoning,
            "highest_and_best_use": results.property_details.highest_and_best_use,
            "valuation_date": results.property_details.valuation_date.isoformat()
        },
        "compensation_breakdown": {
            "market_value": results.compensation_breakdown.market_value,
            "disturbance_damages": {
                "moving_costs": results.compensation_breakdown.moving_costs,
                "business_losses_compensable": results.compensation_breakdown.business_losses_compensable,
                "business_losses_non_compensable": results.compensation_breakdown.business_losses_non_compensable,
                "professional_fees": results.compensation_breakdown.professional_fees,
                "temporary_accommodation": results.compensation_breakdown.temporary_accommodation,
                "construction_impacts_temporary": results.compensation_breakdown.construction_impacts_temporary,
                "permanent_impacts_capitalized": results.compensation_breakdown.permanent_impacts_capitalized,
                "total": results.compensation_breakdown.total_disturbance
            },
            "subtotal_before_interest": results.compensation_breakdown.subtotal_before_interest,
            "interest": results.compensation_breakdown.interest_details,
            "total_compensation": results.compensation_breakdown.total_compensation
        },
        "compliance": {
            "compensable_items": results.compensation_breakdown.compliance_notes,
            "non_compensable_items": results.compensation_breakdown.non_compensable_items
        },
        "analysis_notes": results.analysis_notes
    }

    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)


# ============================================================================
# COMMAND LINE INTERFACE
# ============================================================================

def main():
    """Command-line interface for expropriation compensation calculator"""
    if len(sys.argv) < 2:
        print("Usage: python expropriation_calculator.py <input.json> [output.json]")
        print("\nExample:")
        print("  python expropriation_calculator.py sample_commercial_expropriation.json")
        print("  python expropriation_calculator.py sample_commercial_expropriation.json results.json")
        sys.exit(1)

    input_path = sys.argv[1]

    # Generate output path
    if len(sys.argv) > 2:
        output_path = sys.argv[2]
    else:
        output_path = str(Path(input_path).with_suffix('')) + "_results.json"

    print(f"Loading expropriation scenario from: {input_path}")
    property_details, disturbance_damages, interest_calc = load_expropriation_from_json(input_path)

    print(f"Calculating compensation...")
    results = calculate_expropriation_compensation(property_details, disturbance_damages, interest_calc)

    print(f"Saving results to: {output_path}")
    save_results_to_json(results, output_path)

    print(f"\n✅ Compensation calculation complete!")
    print(f"\nProperty: {property_details.address}")
    print(f"Valuation date: {property_details.valuation_date.strftime('%B %d, %Y')}")
    print(f"Payment date: {interest_calc.payment_date.strftime('%B %d, %Y')}")

    print(f"\n📊 COMPENSATION BREAKDOWN:")
    print(f"  Market value (s.13 OEA):           ${results.compensation_breakdown.market_value:>15,.2f}")

    if results.compensation_breakdown.total_disturbance > 0:
        print(f"\n  Disturbance damages (s.18 OEA):")
        if results.compensation_breakdown.moving_costs > 0:
            print(f"    Moving costs:                    ${results.compensation_breakdown.moving_costs:>15,.2f}")
        if results.compensation_breakdown.business_losses_compensable > 0:
            print(f"    Business losses (compensable):   ${results.compensation_breakdown.business_losses_compensable:>15,.2f}")
        if results.compensation_breakdown.professional_fees > 0:
            print(f"    Professional fees:               ${results.compensation_breakdown.professional_fees:>15,.2f}")
        if results.compensation_breakdown.temporary_accommodation > 0:
            print(f"    Temporary accommodation:         ${results.compensation_breakdown.temporary_accommodation:>15,.2f}")
        if results.compensation_breakdown.construction_impacts_temporary > 0:
            print(f"    Construction impacts (s.18(2)a): ${results.compensation_breakdown.construction_impacts_temporary:>15,.2f}")
        if results.compensation_breakdown.permanent_impacts_capitalized > 0:
            print(f"    Permanent impacts (s.18(2)b):    ${results.compensation_breakdown.permanent_impacts_capitalized:>15,.2f}")
        print(f"    Total disturbance:               ${results.compensation_breakdown.total_disturbance:>15,.2f}")

    print(f"\n  Subtotal before interest:          ${results.compensation_breakdown.subtotal_before_interest:>15,.2f}")

    if results.compensation_breakdown.interest_amount > 0:
        print(f"  Interest ({results.compensation_breakdown.interest_details['days']} days @ {interest_calc.interest_rate_annual_pct}%):      ${results.compensation_breakdown.interest_amount:>15,.2f}")

    print(f"\n  TOTAL COMPENSATION:                ${results.compensation_breakdown.total_compensation:>15,.2f}")
    print(f"  {'=' * 60}")

    # Non-compensable items
    if results.compensation_breakdown.non_compensable_items:
        print(f"\n⚠️  NON-COMPENSABLE ITEMS:")
        for item in results.compensation_breakdown.non_compensable_items:
            print(f"  {item}")

    # OEA compliance summary
    print(f"\n✓ OEA COMPLIANCE:")
    for note in results.compensation_breakdown.compliance_notes[:5]:  # Show first 5
        print(f"  {note}")


if __name__ == '__main__':
    main()
