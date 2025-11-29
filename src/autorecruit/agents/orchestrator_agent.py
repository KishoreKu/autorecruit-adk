"""
High-level orchestrator stub.
Wire together:
- JobIntakeAgent
- CandidateSourcingAgent
- CandidateScreeningAgent
- OutreachAgent
"""

from autorecruit.memory.session_memory import SessionState
from autorecruit.tools.pipeline_logger_tool import log_pipeline_event
from autorecruit.agents.candidate_sourcing_agent import run_candidate_sourcing_agent
from autorecruit.agents.outreach_agent import generate_outreach_emails
# from autorecruit.agents.job_intake_agent import run_job_intake_agent
# from autorecruit.agents.candidate_screening_agent import run_candidate_screening_agent


def run_orchestrator(job_description: str):
    session = SessionState(job_description)
    log_pipeline_event(session.session_id, "session_created", {})

    # 1) Job intake (TODO: implement ADK agent)
    # session.job_profile = run_job_intake_agent(job_description)
    # For now, stub a minimal profile:
    session.job_profile = {
        "title": "Senior Data Engineer",
        "location": "New York, NY",
        "must_have_skills": ["Python", "PySpark", "AWS", "SQL"],
        "min_years_experience": 5,
    }
    log_pipeline_event(session.session_id, "job_intake_done", session.job_profile)

    # 2) Candidate sourcing
    session.candidate_list = run_candidate_sourcing_agent(session.job_profile)
    log_pipeline_event(session.session_id, "candidate_sourcing_done", {"num_candidates": len(session.candidate_list)})

    # 3) Candidate screening (TODO: implement ADK agent)
    # session.screened_candidates = run_candidate_screening_agent(session.job_profile, session.candidate_list)
    # For now, just treat all as shortlisted:
    session.screened_candidates = session.candidate_list

    # 4) Outreach
    session.outreach_emails = generate_outreach_emails(session.job_profile, session.screened_candidates)
    log_pipeline_event(session.session_id, "outreach_generated", {"num_emails": len(session.outreach_emails)})

    return session
