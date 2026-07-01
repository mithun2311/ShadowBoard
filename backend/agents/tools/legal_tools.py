from typing import Dict


def assess_compliance(
    has_privacy_policy: bool,
    has_terms: bool,
    stores_personal_data: bool,
) -> Dict:
    """
    Basic compliance assessment.
    """

    issues = []

    if not has_privacy_policy:
        issues.append("Missing Privacy Policy.")

    if not has_terms:
        issues.append("Missing Terms & Conditions.")

    if stores_personal_data and not has_privacy_policy:
        issues.append(
            "Collecting personal data without a Privacy Policy."
        )

    return {
        "compliant": len(issues) == 0,
        "issues": issues,
    }


def identify_legal_risk(
    severity: str,
) -> Dict:

    mapping = {
        "LOW": "Monitor periodically.",
        "MEDIUM": "Review with legal team.",
        "HIGH": "Immediate legal review required.",
        "CRITICAL": "Executive escalation required.",
    }

    return {
        "severity": severity.upper(),
        "recommendation": mapping.get(
            severity.upper(),
            "Unknown"
        )
    }