from app.services.lyzr.orchestrator import orchestrator

result = orchestrator.prepare_workflow_context(
    "Should ShadowBoard launch next month?"
)

print(result)