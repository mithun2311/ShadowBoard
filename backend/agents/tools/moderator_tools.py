from typing import Dict


def summarize_votes(
    approvals: int,
    rejections: int,
) -> Dict:

    total = approvals + rejections

    if total == 0:
        return {
            "result": "No votes."
        }

    approval_rate = (
        approvals / total
    ) * 100

    decision = (
        "APPROVED"
        if approvals > rejections
        else "REJECTED"
    )

    return {
        "approval_rate": round(
            approval_rate,
            2,
        ),
        "decision": decision,
    }


def consensus_score(
    agreement: int,
    total: int,
) -> Dict:

    if total == 0:
        return {
            "score": 0
        }

    return {
        "consensus_score":
        round(
            agreement / total * 100,
            2,
        )
    }