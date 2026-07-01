from typing import Dict


def estimate_campaign(
    budget: float,
    expected_leads: int,
) -> Dict:

    if expected_leads <= 0:
        return {
            "error": "Expected leads must be greater than zero."
        }

    cost_per_lead = budget / expected_leads

    return {
        "budget": budget,
        "expected_leads": expected_leads,
        "cost_per_lead": round(cost_per_lead, 2),
    }


def recommend_channel(
    audience: str,
) -> Dict:

    mapping = {
        "students": "LinkedIn + Instagram",
        "developers": "GitHub + LinkedIn + Dev Communities",
        "enterprise": "LinkedIn + Email Outreach",
        "startup": "LinkedIn + Product Hunt",
    }

    return {
        "recommended_channel":
            mapping.get(
                audience.lower(),
                "LinkedIn"
            )
    }