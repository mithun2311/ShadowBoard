from typing import Dict


def prioritize_feature(
    business_value: int,
    customer_impact: int,
    technical_effort: int,
) -> Dict:
    """
    Simple feature priority score.
    """

    score = (
        business_value +
        customer_impact
    ) - technical_effort

    if score >= 12:
        priority = "HIGH"
    elif score >= 8:
        priority = "MEDIUM"
    else:
        priority = "LOW"

    return {
        "priority_score": score,
        "priority": priority,
    }


def estimate_release(
    features: int,
    sprint_capacity: int,
) -> Dict:
    """
    Estimate number of sprints required.
    """

    sprints = (
        features +
        sprint_capacity - 1
    ) // sprint_capacity

    return {
        "estimated_sprints": sprints,
    }