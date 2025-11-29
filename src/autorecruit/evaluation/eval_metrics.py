def compute_skill_match(job_profile: dict, candidate: dict) -> float:
    required = set(s.strip().lower() for s in job_profile.get("must_have_skills", []))
    skills = set(s.strip().lower() for s in candidate["primary_skills"].split(","))
    if not required:
        return 0.0
    return len(required & skills) / len(required)
