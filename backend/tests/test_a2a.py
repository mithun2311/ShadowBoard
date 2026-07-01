from app.schemas.executive_response import ExecutiveResponse
from app.services.a2a.collaboration import build_executive_packet

responses = [
    ExecutiveResponse(
        agent="Engineering",
        executive_summary="Platform is technically ready.",
        detailed_analysis="Infrastructure and APIs are stable.",
        risks=["Minor scalability testing pending"],
        recommendations=["Proceed with launch"],
        confidence_score=94,
    ),
    ExecutiveResponse(
        agent="Risk",
        executive_summary="Overall operational risk is low.",
        detailed_analysis="No critical blockers identified.",
        risks=["Monitor production usage"],
        recommendations=["Deploy with monitoring enabled"],
        confidence_score=91,
    ),
]

print(build_executive_packet(responses))