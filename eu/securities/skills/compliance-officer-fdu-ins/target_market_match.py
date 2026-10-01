#!/usr/bin/env python3
"""
EU MiFID II / IDD Target Market Matching Tool

This script assesses whether a client profile matches a product's target market
definition under MiFID II product governance requirements (C(EU) 2017/653) and
IDD product oversight and governance (EIOPA Guidelines).

CRITICAL: This tool implements exact MiFID II/IDD target market matching logic.
DO NOT perform target market assessments manually - use this validated script.

Why this matters for EU compliance:
- MiFID II requires products only be sold to clients within target market
- Sales outside target market trigger enhanced procedures and reporting
- NCAs heavily scrutinize target market compliance
- Poor target market processes = significant fines and remediation costs
- Product governance failures are a top supervisory priority for ESMA

Target Market Dimensions (MiFID II):
1. Type of clients (retail, professional, eligible counterparties)
2. Knowledge and experience
3. Financial situation with focus on ability to bear losses
4. Risk tolerance and compatibility with risk/reward profile
5. Client objectives and needs

Usage:
    python target_market_match.py \\
        --client-type retail \\
        --client-knowledge basic \\
        --client-experience 2 \\
        --client-risk-tolerance low \\
        --client-loss-capacity 10 \\
        --client-time-horizon 5 \\
        --client-objectives capital_preservation \\
        --product-target-retail true \\
        --product-knowledge-required basic \\
        --product-min-experience 1 \\
        --product-risk-level low \\
        --product-max-loss 10 \\
        --product-min-horizon 3 \\
        --product-objectives capital_preservation,income \\
        --output match_result.json

Regulatory References:
- MiFID II Delegated Directive (EU) 2017/593 Articles 9, 10
- Commission Delegated Regulation (EU) 2017/2359
- ESMA Guidelines on MiFID II product governance (ESMA35-43-620)

Author: Financial Services Skill System
Version: 1.0.0
Last Updated: November 2024
"""

import argparse
import json
import sys
from typing import Dict, Any, List, Set
from datetime import datetime


class TargetMarketMatcher:
    """
    Assess client-product target market matching per MiFID II/IDD.

    Implements exact matching logic from:
    - MiFID II Delegated Directive (EU) 2017/593
    - ESMA Guidelines on MiFID II product governance
    - IDD Delegated Regulation (EU) 2017/2359
    """

    # Knowledge levels
    KNOWLEDGE_LEVELS = ["none", "basic", "informed", "advanced"]

    # Risk tolerance levels
    RISK_LEVELS = ["no_risk", "low", "medium", "high", "very_high"]

    # Client types
    CLIENT_TYPES = ["retail", "professional", "eligible_counterparty"]

    # Client objectives
    VALID_OBJECTIVES = [
        "capital_preservation",
        "income",
        "growth",
        "speculation",
        "hedging",
        "portfolio_diversification",
        "esg_aligned"
    ]

    def __init__(self):
        """Initialize target market matcher."""
        pass

    def assess_target_market_match(
        self,
        # Client profile
        client_type: str,
        client_knowledge: str,
        client_experience_years: int,
        client_risk_tolerance: str,
        client_loss_capacity_percent: float,
        client_time_horizon_years: int,
        client_objectives: List[str],
        client_financial_situation_adequate: bool = True,

        # Product target market
        product_target_retail: bool = False,
        product_target_professional: bool = False,
        product_target_eligible_counterparty: bool = False,
        product_knowledge_required: str = "basic",
        product_min_experience_years: int = 0,
        product_risk_level: str = "low",
        product_max_loss_percent: float = 100,
        product_min_time_horizon_years: int = 0,
        product_objectives: List[str] = None,
        product_complex: bool = False,

        # Distribution channel
        distribution_with_advice: bool = True,
    ) -> Dict[str, Any]:
        """
        Assess whether client matches product target market.

        Args:
            CLIENT PROFILE:
            client_type: retail, professional, or eligible_counterparty
            client_knowledge: none, basic, informed, or advanced
            client_experience_years: Years of investment experience
            client_risk_tolerance: no_risk, low, medium, high, very_high
            client_loss_capacity_percent: Maximum loss client can bear (% of investment)
            client_time_horizon_years: Client's investment time horizon
            client_objectives: List of client objectives
            client_financial_situation_adequate: Can client afford to invest

            PRODUCT TARGET MARKET:
            product_target_retail: Product suitable for retail clients
            product_target_professional: Product suitable for professional clients
            product_target_eligible_counterparty: Product suitable for ECPs
            product_knowledge_required: Minimum knowledge level required
            product_min_experience_years: Minimum experience required
            product_risk_level: Product risk level
            product_max_loss_percent: Maximum potential loss
            product_min_time_horizon_years: Minimum recommended holding period
            product_objectives: Product objectives (what needs it serves)
            product_complex: Is product complex (MiFID II definition)

            DISTRIBUTION:
            distribution_with_advice: Is advice being provided

        Returns:
            Comprehensive target market matching assessment
        """
        # Validate inputs
        self._validate_inputs(
            client_type, client_knowledge, client_risk_tolerance,
            product_knowledge_required, product_risk_level
        )

        if product_objectives is None:
            product_objectives = []

        # Assess each target market dimension
        client_type_match = self._assess_client_type(
            client_type,
            product_target_retail,
            product_target_professional,
            product_target_eligible_counterparty
        )

        knowledge_match = self._assess_knowledge_experience(
            client_knowledge,
            client_experience_years,
            product_knowledge_required,
            product_min_experience_years,
            product_complex,
            distribution_with_advice
        )

        financial_situation_match = self._assess_financial_situation(
            client_financial_situation_adequate,
            client_loss_capacity_percent,
            product_max_loss_percent
        )

        risk_match = self._assess_risk_compatibility(
            client_risk_tolerance,
            product_risk_level
        )

        objectives_match = self._assess_objectives_needs(
            client_objectives,
            product_objectives
        )

        time_horizon_match = self._assess_time_horizon(
            client_time_horizon_years,
            product_min_time_horizon_years
        )

        # Determine overall match
        overall_assessment = self._determine_overall_match(
            client_type_match,
            knowledge_match,
            financial_situation_match,
            risk_match,
            objectives_match,
            time_horizon_match
        )

        # Generate compliance actions
        compliance_actions = self._generate_compliance_actions(
            overall_assessment,
            client_type_match,
            knowledge_match,
            financial_situation_match,
            risk_match,
            objectives_match,
            time_horizon_match,
            distribution_with_advice
        )

        # Compile result
        result = {
            "assessment_timestamp": datetime.now().isoformat(),
            "regulatory_framework": "MiFID II / IDD Product Governance",

            "client_profile": {
                "client_type": client_type,
                "knowledge": client_knowledge,
                "experience_years": client_experience_years,
                "risk_tolerance": client_risk_tolerance,
                "loss_capacity_percent": client_loss_capacity_percent,
                "time_horizon_years": client_time_horizon_years,
                "objectives": client_objectives,
                "financial_situation_adequate": client_financial_situation_adequate
            },

            "product_target_market": {
                "target_client_types": self._get_target_client_types(
                    product_target_retail,
                    product_target_professional,
                    product_target_eligible_counterparty
                ),
                "knowledge_required": product_knowledge_required,
                "min_experience_years": product_min_experience_years,
                "risk_level": product_risk_level,
                "max_loss_percent": product_max_loss_percent,
                "min_time_horizon_years": product_min_time_horizon_years,
                "objectives": product_objectives,
                "complex": product_complex
            },

            "distribution_context": {
                "with_advice": distribution_with_advice,
                "service_type": "Investment Advice" if distribution_with_advice else "Execution Only"
            },

            "dimension_assessments": {
                "client_type": client_type_match,
                "knowledge_experience": knowledge_match,
                "financial_situation": financial_situation_match,
                "risk_tolerance": risk_match,
                "objectives_needs": objectives_match,
                "time_horizon": time_horizon_match
            },

            "overall_assessment": overall_assessment,
            "compliance_actions": compliance_actions,

            "regulatory_references": [
                "MiFID II Delegated Directive (EU) 2017/593 Articles 9-10",
                "ESMA Guidelines on MiFID II product governance (ESMA35-43-620)",
                "IDD Delegated Regulation (EU) 2017/2359"
            ]
        }

        return result

    def _validate_inputs(
        self,
        client_type: str,
        client_knowledge: str,
        client_risk_tolerance: str,
        product_knowledge_required: str,
        product_risk_level: str
    ):
        """Validate enumerated inputs."""
        if client_type not in self.CLIENT_TYPES:
            raise ValueError(f"Invalid client_type. Must be one of: {self.CLIENT_TYPES}")

        if client_knowledge not in self.KNOWLEDGE_LEVELS:
            raise ValueError(f"Invalid client_knowledge. Must be one of: {self.KNOWLEDGE_LEVELS}")

        if client_risk_tolerance not in self.RISK_LEVELS:
            raise ValueError(f"Invalid client_risk_tolerance. Must be one of: {self.RISK_LEVELS}")

        if product_knowledge_required not in self.KNOWLEDGE_LEVELS:
            raise ValueError(f"Invalid product_knowledge_required. Must be one of: {self.KNOWLEDGE_LEVELS}")

        if product_risk_level not in self.RISK_LEVELS:
            raise ValueError(f"Invalid product_risk_level. Must be one of: {self.RISK_LEVELS}")

    def _get_target_client_types(
        self,
        retail: bool,
        professional: bool,
        ecp: bool
    ) -> List[str]:
        """Get list of target client types."""
        types = []
        if retail:
            types.append("retail")
        if professional:
            types.append("professional")
        if ecp:
            types.append("eligible_counterparty")
        return types

    def _assess_client_type(
        self,
        client_type: str,
        target_retail: bool,
        target_professional: bool,
        target_ecp: bool
    ) -> Dict[str, Any]:
        """Assess if client type matches target market."""
        target_types = self._get_target_client_types(target_retail, target_professional, target_ecp)

        if not target_types:
            return {
                "match": "ERROR",
                "client_type": client_type,
                "target_types": [],
                "explanation": "ERROR: Product has no defined target client types. This violates MiFID II product governance requirements."
            }

        matches = client_type in target_types

        return {
            "match": "POSITIVE" if matches else "NEGATIVE",
            "client_type": client_type,
            "target_types": target_types,
            "in_target": matches,
            "explanation": f"Client type '{client_type}' is {'within' if matches else 'OUTSIDE'} target market." if matches else f"❌ Client type '{client_type}' is outside target market. Product targets: {target_types}."
        }

    def _assess_knowledge_experience(
        self,
        client_knowledge: str,
        client_experience: int,
        required_knowledge: str,
        required_experience: int,
        product_complex: bool,
        with_advice: bool
    ) -> Dict[str, Any]:
        """Assess knowledge and experience matching."""
        knowledge_index = self.KNOWLEDGE_LEVELS.index(client_knowledge)
        required_knowledge_index = self.KNOWLEDGE_LEVELS.index(required_knowledge)

        knowledge_sufficient = knowledge_index >= required_knowledge_index
        experience_sufficient = client_experience >= required_experience

        # For complex products without advice, stricter requirements apply
        if product_complex and not with_advice:
            # Appropriateness test applies (execution-only)
            # Client must have adequate knowledge and experience
            if not (knowledge_sufficient and experience_sufficient):
                match = "NEGATIVE"
                explanation = f"❌ Complex product sold execution-only requires adequate knowledge/experience. Client has '{client_knowledge}' knowledge and {client_experience} years experience, but product requires '{required_knowledge}' and {required_experience} years minimum."
            else:
                match = "POSITIVE"
                explanation = f"✅ Client has adequate knowledge ('{client_knowledge}' >= '{required_knowledge}') and experience ({client_experience} >= {required_experience} years) for complex product execution-only."
        else:
            # With advice, knowledge/experience requirements are less critical
            # But still part of target market assessment
            if knowledge_sufficient and experience_sufficient:
                match = "POSITIVE"
                explanation = f"✅ Client knowledge ('{client_knowledge}') and experience ({client_experience} years) meet target market requirements."
            elif knowledge_sufficient or experience_sufficient:
                match = "NEUTRAL"
                explanation = f"⚠️ Client partially meets knowledge/experience requirements. Knowledge: '{client_knowledge}' (required: '{required_knowledge}'), Experience: {client_experience} years (required: {required_experience}). With advice, may still be suitable."
            else:
                match = "NEGATIVE"
                explanation = f"❌ Client knowledge ('{client_knowledge}') and experience ({client_experience} years) below target market requirements ('{required_knowledge}', {required_experience} years)."

        return {
            "match": match,
            "client_knowledge": client_knowledge,
            "client_experience_years": client_experience,
            "required_knowledge": required_knowledge,
            "required_experience_years": required_experience,
            "knowledge_sufficient": knowledge_sufficient,
            "experience_sufficient": experience_sufficient,
            "product_complex": product_complex,
            "with_advice": with_advice,
            "explanation": explanation
        }

    def _assess_financial_situation(
        self,
        adequate: bool,
        client_loss_capacity: float,
        product_max_loss: float
    ) -> Dict[str, Any]:
        """Assess financial situation and ability to bear losses."""
        if not adequate:
            return {
                "match": "NEGATIVE",
                "client_financial_situation_adequate": False,
                "explanation": "❌ Client's financial situation is not adequate for investment products. Client should not invest."
            }

        loss_capacity_adequate = client_loss_capacity >= product_max_loss

        if loss_capacity_adequate:
            match = "POSITIVE"
            explanation = f"✅ Client can bear potential losses. Loss capacity: {client_loss_capacity}%, Product max loss: {product_max_loss}%."
        else:
            match = "NEGATIVE"
            explanation = f"❌ Client's loss capacity ({client_loss_capacity}%) is BELOW product's maximum potential loss ({product_max_loss}%). Client cannot afford this product."

        return {
            "match": match,
            "client_loss_capacity_percent": client_loss_capacity,
            "product_max_loss_percent": product_max_loss,
            "loss_capacity_adequate": loss_capacity_adequate,
            "explanation": explanation
        }

    def _assess_risk_compatibility(
        self,
        client_risk_tolerance: str,
        product_risk_level: str
    ) -> Dict[str, Any]:
        """Assess risk tolerance compatibility."""
        client_risk_index = self.RISK_LEVELS.index(client_risk_tolerance)
        product_risk_index = self.RISK_LEVELS.index(product_risk_level)

        compatible = client_risk_index >= product_risk_index

        if compatible:
            match = "POSITIVE"
            explanation = f"✅ Client risk tolerance ('{client_risk_tolerance}') compatible with product risk level ('{product_risk_level}')."
        else:
            match = "NEGATIVE"
            explanation = f"❌ Product risk level ('{product_risk_level}') EXCEEDS client's risk tolerance ('{client_risk_tolerance}'). Incompatible."

        return {
            "match": match,
            "client_risk_tolerance": client_risk_tolerance,
            "product_risk_level": product_risk_level,
            "compatible": compatible,
            "explanation": explanation
        }

    def _assess_objectives_needs(
        self,
        client_objectives: List[str],
        product_objectives: List[str]
    ) -> Dict[str, Any]:
        """Assess whether product objectives align with client objectives."""
        if not product_objectives:
            return {
                "match": "NEUTRAL",
                "client_objectives": client_objectives,
                "product_objectives": [],
                "overlap": [],
                "explanation": "⚠️ Product has no defined objectives. Cannot assess alignment."
            }

        client_set = set(client_objectives)
        product_set = set(product_objectives)
        overlap = client_set.intersection(product_set)

        if overlap:
            match = "POSITIVE"
            explanation = f"✅ Product objectives align with client objectives. Overlap: {list(overlap)}."
        elif client_objectives and product_objectives:
            match = "NEGATIVE"
            explanation = f"❌ No alignment between client objectives ({client_objectives}) and product objectives ({product_objectives})."
        else:
            match = "NEUTRAL"
            explanation = "⚠️ Insufficient objective information to assess alignment."

        return {
            "match": match,
            "client_objectives": client_objectives,
            "product_objectives": product_objectives,
            "overlap": list(overlap),
            "explanation": explanation
        }

    def _assess_time_horizon(
        self,
        client_horizon: int,
        product_min_horizon: int
    ) -> Dict[str, Any]:
        """Assess time horizon compatibility."""
        adequate = client_horizon >= product_min_horizon

        if adequate:
            match = "POSITIVE"
            explanation = f"✅ Client time horizon ({client_horizon} years) meets product minimum ({product_min_horizon} years)."
        else:
            match = "NEGATIVE"
            explanation = f"❌ Client time horizon ({client_horizon} years) is SHORTER than product minimum recommended holding period ({product_min_horizon} years). Incompatible."

        return {
            "match": match,
            "client_time_horizon_years": client_horizon,
            "product_min_horizon_years": product_min_horizon,
            "adequate": adequate,
            "explanation": explanation
        }

    def _determine_overall_match(
        self,
        client_type: Dict,
        knowledge: Dict,
        financial: Dict,
        risk: Dict,
        objectives: Dict,
        time_horizon: Dict
    ) -> Dict[str, Any]:
        """Determine overall target market match."""
        # Critical dimensions (must match)
        critical_negative = (
            client_type["match"] == "NEGATIVE" or
            financial["match"] == "NEGATIVE" or
            risk["match"] == "NEGATIVE" or
            time_horizon["match"] == "NEGATIVE"
        )

        # Important dimensions
        knowledge_negative = knowledge["match"] == "NEGATIVE"
        objectives_negative = objectives["match"] == "NEGATIVE"

        if critical_negative:
            overall_match = "OUTSIDE_TARGET_MARKET"
            category = "Negative Target Market"
            recommendation = "DO NOT PROCEED with this sale. Product is outside client's target market."
            regulatory_action = "Sale must not proceed unless exceptional circumstances documented and senior management approval obtained."
        elif knowledge_negative or objectives_negative:
            overall_match = "OUTSIDE_POSITIVE_TARGET_MARKET"
            category = "Outside Positive Target Market (but not negative)"
            recommendation = "Enhanced procedures required. Document why product is still suitable despite being outside positive target market."
            regulatory_action = "Enhanced assessment required. Consider alternative products. If proceeding, document rationale and obtain additional approvals per firm's product governance procedures."
        else:
            overall_match = "WITHIN_TARGET_MARKET"
            category = "Within Positive Target Market"
            recommendation = "Product appears compatible with client profile based on target market assessment."
            regulatory_action = "Proceed with full suitability assessment (if advice) or sale (if execution-only)."

        return {
            "overall_match": overall_match,
            "category": category,
            "recommendation": recommendation,
            "regulatory_action": regulatory_action,
            "critical_mismatches": critical_negative,
            "requires_enhanced_procedures": overall_match != "WITHIN_TARGET_MARKET"
        }

    def _generate_compliance_actions(
        self,
        overall: Dict,
        client_type: Dict,
        knowledge: Dict,
        financial: Dict,
        risk: Dict,
        objectives: Dict,
        time_horizon: Dict,
        with_advice: bool
    ) -> List[str]:
        """Generate required compliance actions based on assessment."""
        actions = []

        if overall["overall_match"] == "OUTSIDE_TARGET_MARKET":
            actions.append("🛑 STOP: Do not proceed with sale")
            actions.append("📋 Document why client is in negative target market")
            actions.append("👔 Escalate to senior management and compliance")
            actions.append("📊 Record sale attempt in product governance MI")
            actions.append("🔍 Consider if product design requires review")

        elif overall["overall_match"] == "OUTSIDE_POSITIVE_TARGET_MARKET":
            actions.append("⚠️ Enhanced procedures required")
            actions.append("📋 Document why product is still considered suitable")
            actions.append("🔍 Consider alternative products within target market")
            actions.append("✅ Obtain additional approval (as per firm procedures)")
            actions.append("📊 Report to product governance function")
            if with_advice:
                actions.append("📝 Enhanced suitability assessment required")
                actions.append("⚠️ Include warning in suitability report about target market")

        else:  # WITHIN_TARGET_MARKET
            actions.append("✅ Proceed with standard sales process")
            if with_advice:
                actions.append("📝 Complete suitability assessment")
                actions.append("📄 Prepare suitability report")
            else:
                actions.append("📝 Complete appropriateness test (if complex product)")
            actions.append("💰 Provide costs and charges disclosure")
            actions.append("📋 Maintain records per MiFID II requirements")

        # Specific dimension warnings
        if client_type["match"] == "NEGATIVE":
            actions.append(f"❌ Client type mismatch: {client_type['explanation']}")

        if financial["match"] == "NEGATIVE":
            actions.append(f"❌ Financial situation inadequate: {financial['explanation']}")

        if knowledge["match"] == "NEGATIVE" and knowledge.get("product_complex") and not knowledge.get("with_advice"):
            actions.append("❌ Appropriateness test FAILED - cannot proceed with execution-only sale of complex product")

        return actions


def main():
    """Command-line interface for Target Market Matcher."""
    parser = argparse.ArgumentParser(
        description="EU MiFID II/IDD Target Market Matching Assessment",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Retail client, basic product, within target market
  python target_market_match.py --client-type retail --client-knowledge informed --client-experience 3 \\
      --client-risk-tolerance medium --client-loss-capacity 20 --client-time-horizon 5 \\
      --client-objectives growth,income --product-target-retail true --product-knowledge-required basic \\
      --product-min-experience 1 --product-risk-level medium --product-max-loss 20 \\
      --product-min-horizon 3 --product-objectives growth,income

  # High-risk product, low-risk client (mismatch)
  python target_market_match.py --client-type retail --client-knowledge basic --client-experience 1 \\
      --client-risk-tolerance low --client-loss-capacity 5 --client-time-horizon 2 \\
      --client-objectives capital_preservation --product-target-retail true --product-knowledge-required advanced \\
      --product-min-experience 5 --product-risk-level very_high --product-max-loss 100 \\
      --product-min-horizon 10 --product-objectives speculation --product-complex true

  # Complex product execution-only (appropriateness test)
  python target_market_match.py --client-type retail --client-knowledge informed --client-experience 5 \\
      --client-risk-tolerance high --client-loss-capacity 50 --client-time-horizon 7 \\
      --client-objectives growth --product-target-retail true --product-knowledge-required informed \\
      --product-min-experience 3 --product-risk-level high --product-max-loss 50 \\
      --product-min-horizon 5 --product-objectives growth --product-complex true \\
      --distribution-with-advice false

Output: JSON file with comprehensive target market matching assessment
        """
    )

    # Client profile
    client_group = parser.add_argument_group('Client Profile')
    client_group.add_argument("--client-type", required=True, choices=["retail", "professional", "eligible_counterparty"])
    client_group.add_argument("--client-knowledge", required=True, choices=["none", "basic", "informed", "advanced"])
    client_group.add_argument("--client-experience", type=int, required=True, help="Years of investment experience")
    client_group.add_argument("--client-risk-tolerance", required=True, choices=["no_risk", "low", "medium", "high", "very_high"])
    client_group.add_argument("--client-loss-capacity", type=float, required=True, help="Maximum loss capacity (percent of investment)")
    client_group.add_argument("--client-time-horizon", type=int, required=True, help="Investment time horizon (years)")
    client_group.add_argument("--client-objectives", required=True, help="Comma-separated list of objectives")
    client_group.add_argument("--client-financial-adequate", type=lambda x: x.lower() == 'true', default=True, help="Financial situation adequate (true/false)")

    # Product target market
    product_group = parser.add_argument_group('Product Target Market')
    product_group.add_argument("--product-target-retail", type=lambda x: x.lower() == 'true', default=False)
    product_group.add_argument("--product-target-professional", type=lambda x: x.lower() == 'true', default=False)
    product_group.add_argument("--product-target-ecp", type=lambda x: x.lower() == 'true', default=False)
    product_group.add_argument("--product-knowledge-required", required=True, choices=["none", "basic", "informed", "advanced"])
    product_group.add_argument("--product-min-experience", type=int, required=True, help="Minimum experience required (years)")
    product_group.add_argument("--product-risk-level", required=True, choices=["no_risk", "low", "medium", "high", "very_high"])
    product_group.add_argument("--product-max-loss", type=float, required=True, help="Maximum potential loss (percent)")
    product_group.add_argument("--product-min-horizon", type=int, required=True, help="Minimum recommended holding period (years)")
    product_group.add_argument("--product-objectives", default="", help="Comma-separated list of product objectives")
    product_group.add_argument("--product-complex", type=lambda x: x.lower() == 'true', default=False, help="Is product complex per MiFID II")

    # Distribution
    dist_group = parser.add_argument_group('Distribution Context')
    dist_group.add_argument("--distribution-with-advice", type=lambda x: x.lower() == 'true', default=True, help="With investment advice (true/false)")

    # Output
    parser.add_argument("--output", default="target_market_match.json", help="Output JSON file")

    args = parser.parse_args()

    # Parse objectives
    client_objectives = [obj.strip() for obj in args.client_objectives.split(',') if obj.strip()]
    product_objectives = [obj.strip() for obj in args.product_objectives.split(',') if obj.strip()] if args.product_objectives else []

    # Create matcher
    matcher = TargetMarketMatcher()

    try:
        # Run assessment
        result = matcher.assess_target_market_match(
            client_type=args.client_type,
            client_knowledge=args.client_knowledge,
            client_experience_years=args.client_experience,
            client_risk_tolerance=args.client_risk_tolerance,
            client_loss_capacity_percent=args.client_loss_capacity,
            client_time_horizon_years=args.client_time_horizon,
            client_objectives=client_objectives,
            client_financial_situation_adequate=args.client_financial_adequate,
            product_target_retail=args.product_target_retail,
            product_target_professional=args.product_target_professional,
            product_target_eligible_counterparty=args.product_target_ecp,
            product_knowledge_required=args.product_knowledge_required,
            product_min_experience_years=args.product_min_experience,
            product_risk_level=args.product_risk_level,
            product_max_loss_percent=args.product_max_loss,
            product_min_time_horizon_years=args.product_min_horizon,
            product_objectives=product_objectives,
            product_complex=args.product_complex,
            distribution_with_advice=args.distribution_with_advice,
        )

        # Write to file
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2)

        # Print summary
        print(f"\n{'='*80}")
        print(f"EU MiFID II/IDD TARGET MARKET MATCHING ASSESSMENT")
        print(f"{'='*80}\n")

        overall = result['overall_assessment']
        print(f"Overall Match: {overall['overall_match']}")
        print(f"Category: {overall['category']}\n")

        print(f"Recommendation:")
        print(f"  {overall['recommendation']}\n")

        print(f"Regulatory Action Required:")
        print(f"  {overall['regulatory_action']}\n")

        print("Compliance Actions:")
        for action in result['compliance_actions']:
            print(f"  {action}")

        print(f"\n{'='*80}")
        print(f"Full assessment written to: {args.output}")
        print(f"{'='*80}\n")

        # Exit code based on match result
        if overall['overall_match'] == "OUTSIDE_TARGET_MARKET":
            sys.exit(2)  # Critical - negative target market
        elif overall['overall_match'] == "OUTSIDE_POSITIVE_TARGET_MARKET":
            sys.exit(1)  # Warning - outside positive
        else:
            sys.exit(0)  # Success - within target market

    except ValueError as e:
        print(f"\n❌ ERROR: {str(e)}\n", file=sys.stderr)
        sys.exit(3)
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {str(e)}\n", file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    main()
