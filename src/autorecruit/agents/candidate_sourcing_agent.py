from autorecruit.tools.candidate_search_tool import search_candidates

def run_candidate_sourcing_agent(job_profile: dict):
    return search_candidates(job_profile, top_k=5)
