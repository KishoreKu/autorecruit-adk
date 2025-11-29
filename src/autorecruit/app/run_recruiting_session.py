from autorecruit.agents.orchestrator_agent import run_orchestrator

def run_recruiting_session(job_description: str):
    """
    High-level entry point for the AutoRecruit ADK app.
    Simulates a deployed endpoint.
    """
    return run_orchestrator(job_description)
