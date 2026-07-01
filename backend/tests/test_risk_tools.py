from agents.tools.risk_tools import (
    assess_risk,
    mitigation_plan,
)

risk = assess_risk(
    probability=8,
    impact=9,
)

print(risk)

print()

print(
    mitigation_plan(
        risk["risk_level"]
    )
)