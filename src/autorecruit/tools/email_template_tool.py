def get_email_template(template_type: str = "cold_outreach") -> str:
    if template_type == "cold_outreach":
        return (
            "Subject: {role_title} opportunity with {client_name}\n\n"
            "Hi {candidate_name},\n\n"
            "I came across your background in {candidate_highlights} and thought you might be a great fit for "
            "a {role_title} role with our client in {job_location}. The role involves {role_summary}.\n\n"
            "If you are open to exploring this, please reply with an updated resume and a good time to connect.\n\n"
            "Best regards,\n"
            "{recruiter_name},\n"
            "{company_name}."
        )
    return ""
