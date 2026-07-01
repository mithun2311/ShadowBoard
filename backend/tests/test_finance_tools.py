from agents.tools.finance_tools import (
    calculate_roi,
    estimate_budget,
)

print(calculate_roi(
    investment=100000,
    revenue=160000,
))

print()

print(estimate_budget(
    team_size=5,
    monthly_salary=50000,
    duration_months=6,
))