import uuid

class SessionState:
    def __init__(self, job_description: str):
        self.session_id = f"JOB-{uuid.uuid4().hex[:8]}"
        self.job_description = job_description
        self.job_profile = None
        self.candidate_list = None
        self.screened_candidates = None
        self.outreach_emails = None

memory_bank = {
    "past_jobs": [],
    "contacted_candidates": set(),
}
