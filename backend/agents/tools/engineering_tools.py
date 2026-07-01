from typing import Dict


def estimate_api_effort(
    endpoints: int,
    complexity: str,
) -> Dict:

    factors = {
        "LOW": 1,
        "MEDIUM": 2,
        "HIGH": 3,
    }

    factor = factors.get(complexity.upper(), 2)

    estimated_days = endpoints * factor

    return {
        "estimated_days": estimated_days,
        "complexity": complexity.upper(),
    }


def architecture_review(
    uses_microservices: bool,
    uses_cache: bool,
    uses_database: bool,
) -> Dict:

    score = 0

    if uses_microservices:
        score += 35

    if uses_cache:
        score += 30

    if uses_database:
        score += 35

    return {
        "architecture_score": score,
        "rating": (
            "Excellent"
            if score >= 90
            else "Good"
            if score >= 70
            else "Needs Improvement"
        ),
    }