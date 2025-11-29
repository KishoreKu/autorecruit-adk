from autorecruit.app.run_recruiting_session import run_recruiting_session

if __name__ == "__main__":
    example_jd = "We are looking for a Senior Data Engineer with Python, PySpark, AWS and SQL experience in New York."
    session = run_recruiting_session(example_jd)
    print("Session ID:", session.session_id)
    print("Job profile:", session.job_profile)
    print("Candidates:", session.candidate_list)
    print("Emails:", [e["candidate_name"] for e in session.outreach_emails])
