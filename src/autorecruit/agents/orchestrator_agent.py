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

import re


def _parse_job_profile(job_description: str) -> dict:
    """
    Simple parsing function to extract job profile from job description.
    This is a placeholder for the full JobIntakeAgent implementation.
    """
    profile = {}
    
    # Try to extract title - look for common patterns
    title_match = re.search(r'(?:looking for|seeking|hiring|role:?|position:?)\s+(?:a\s+)?([A-Za-z\s]+?)(?:\s+(?:to|role|position|with|at|in|for)|\.|\n|$)', job_description, re.IGNORECASE)
    if title_match:
        potential_title = title_match.group(1).strip()
        if 5 < len(potential_title) < 100:  # Reasonable title length
            profile["title"] = potential_title
        else:
            profile["title"] = "Senior Data Engineer"
    else:
        profile["title"] = "Senior Data Engineer"
    
    # Try to extract location - look for city, state patterns
    location_match = re.search(r'(?:location|based|located|office|city|remote):?\s*([A-Za-z\s,]+?)(?:\.|$|,|\()', job_description, re.IGNORECASE)
    if location_match:
        location = location_match.group(1).strip()
        if 3 < len(location) < 50:
            profile["location"] = location
        else:
            profile["location"] = "New York, NY"
    else:
        profile["location"] = "New York, NY"
    
    # Extract skills (common tech skills)
    common_skills = [
        "Python", "Java", "JavaScript", "C++", "C#", "Go", "Rust", "Ruby", "PHP",
        "SQL", "PostgreSQL", "MySQL", "MongoDB", "Redis", "Cassandra",
        "AWS", "Azure", "GCP", "Google Cloud",
        "Docker", "Kubernetes", "Spark", "PySpark", "Hadoop",
        "React", "Vue", "Angular", "Node.js", "Django", "Flask",
        "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch",
        "Kafka", "Kinesis", "Airflow", "dbt", "Snowflake", "Redshift",
        "Terraform", "CloudFormation", "CI/CD", "DevOps"
    ]
    
    found_skills = []
    for skill in common_skills:
        if re.search(r'\b' + re.escape(skill) + r'\b', job_description, re.IGNORECASE):
            found_skills.append(skill)
    
    if found_skills:
        profile["must_have_skills"] = found_skills[:5]  # Top 5 skills
    else:
        profile["must_have_skills"] = ["Python", "SQL"]
    
    # Try to extract experience requirement
    exp_match = re.search(r'(\d+)\+?\s*(?:years?|yrs?)\s*(?:of\s+)?(?:experience|exp)', job_description, re.IGNORECASE)
    if exp_match:
        profile["min_years_experience"] = int(exp_match.group(1))
    else:
        profile["min_years_experience"] = 5
    
    return profile


def run_orchestrator(job_description: str):
    session = SessionState(job_description)
    log_pipeline_event(session.session_id, "session_created", {})

    # 1) Job intake (TODO: implement ADK agent)
    # session.job_profile = run_job_intake_agent(job_description)
    # For now, parse a minimal profile from the job description:
    session.job_profile = _parse_job_profile(job_description)
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
