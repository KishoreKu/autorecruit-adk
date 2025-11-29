from autorecruit.evaluation.eval_metrics import compute_skill_match

def test_compute_skill_match():
    job_profile = {"must_have_skills": ["Python", "SQL"]}
    candidate = {"primary_skills": "Python,SQL,AWS"}
    score = compute_skill_match(job_profile, candidate)
    assert 0.99 < score <= 1.0
