from autorecruit.tools.email_template_tool import get_email_template

def generate_outreach_emails(job_profile: dict, shortlisted_candidates: list):
    template = get_email_template("cold_outreach")
    emails = []
    for c in shortlisted_candidates:
        candidate_highlights = ", ".join(c["primary_skills"].split(",")[:3])
        filled = template.format(
            role_title=job_profile.get("title", "Data Engineer"),
            client_name="Confidential Client",
            candidate_name=c["name"],
            candidate_highlights=candidate_highlights,
            job_location=job_profile.get("location", "USA"),
            role_summary="building cloud data pipelines",
            recruiter_name="YOUR_NAME_HERE",
            company_name="Westley Resource",
        )
        emails.append(
            {
                "candidate_id": c["candidate_id"],
                "candidate_name": c["name"],
                "email_text": filled,
            }
        )
    return emails
