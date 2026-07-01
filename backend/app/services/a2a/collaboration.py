from typing import List

from app.schemas.executive_response import ExecutiveResponse


def build_executive_packet(
    responses: List[ExecutiveResponse],
) -> str:

    report = []

    for response in responses:

        report.append(
            f"""
Executive: {response.agent}

Summary:
{response.executive_summary}

Analysis:
{response.detailed_analysis}

Risks:
{chr(10).join('- ' + r for r in response.risks)}

Recommendations:
{chr(10).join('- ' + r for r in response.recommendations)}

Confidence:
{response.confidence_score}/100
"""
        )

    return "\n\n".join(report)