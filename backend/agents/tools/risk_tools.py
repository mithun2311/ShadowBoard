from typing import Dict


def assess_risk(
    probability: float,
    impact: float,
) -> Dict:
    """
    Assess project risk using probability and impact.
    Values should be between 0 and 10.
    """

    score = probability * impact

    if score < 20:
        level = "LOW"
    elif score < 40:
        level = "MEDIUM"
    elif score < 70:
        level = "HIGH"
    else:
        level = "CRITICAL"

    return {
        "risk_score": round(score, 2),
        "risk_level": level,
    }


def mitigation_plan(level: str) -> Dict:
    """
    Recommend mitigation based on the risk level.
    """

    plans = {
        "LOW": "Continue monitoring.",
        "MEDIUM": "Create a mitigation plan and review weekly.",
        "HIGH": "Assign an owner and monitor daily.",
        "CRITICAL": "Immediate escalation and executive attention required.",
    }

    return {
        "risk_level": level,
        "recommendation": plans.get(level.upper(), "Unknown risk level."),
    }