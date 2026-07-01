from typing import Dict


def calculate_roi(
    investment: float,
    revenue: float
) -> Dict:
    """
    Calculate Return On Investment.
    """

    if investment <= 0:
        return {
            "error": "Investment must be greater than zero."
        }

    roi = ((revenue - investment) / investment) * 100

    return {
        "investment": investment,
        "revenue": revenue,
        "roi_percentage": round(roi, 2)
    }


def estimate_budget(
    team_size: int,
    monthly_salary: float,
    duration_months: int
) -> Dict:
    """
    Estimate project budget.
    """

    total = (
        team_size *
        monthly_salary *
        duration_months
    )

    return {
        "team_size": team_size,
        "duration_months": duration_months,
        "estimated_budget": total
    }
def cost_breakdown(
    infrastructure: float,
    salaries: float,
    marketing: float,
    contingency: float,
):
    total = (
        infrastructure
        + salaries
        + marketing
        + contingency
    )

    return {
        "Infrastructure": infrastructure,
        "Salaries": salaries,
        "Marketing": marketing,
        "Contingency": contingency,
        "Total": total,
    }