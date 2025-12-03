import streamlit as st
import pandas as pd
import os
import sys
import importlib

# Add the src directory to the path so imports work correctly
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_path = os.path.join(project_root, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Force reimport to avoid caching issues
if 'autorecruit.agents.orchestrator_agent' in sys.modules:
    importlib.reload(sys.modules['autorecruit.agents.orchestrator_agent'])
if 'autorecruit.tools.pipeline_logger_tool' in sys.modules:
    importlib.reload(sys.modules['autorecruit.tools.pipeline_logger_tool'])

from autorecruit.app.run_recruiting_session import run_recruiting_session
from autorecruit.tools.pipeline_logger_tool import pipeline_events


# --- Page config ---
st.set_page_config(
    page_title="AutoRecruit ADK – Recruiting Copilot",
    layout="wide",
)

# --- Example JD (Define before session state initialization) ---
default_jd = """We are looking for a Senior Data Engineer to join our cloud data platform team.

Responsibilities:
- Design and build scalable data pipelines on AWS using PySpark and Spark.
- Work with streaming technologies like Kafka or Kinesis.
- Build and optimize data models in Snowflake and Redshift.
- Collaborate with analytics and ML teams to deliver reliable datasets.

Requirements:
- 7+ years of total experience, with at least 4+ years in data engineering.
- Strong experience with Python, PySpark, SQL.
- Hands-on experience with AWS (S3, EMR, Glue or Databricks).
- Experience with at least one data warehouse: Snowflake or Redshift.
- Experience with orchestration (Airflow or similar).

Nice-to-have:
- Experience with dbt.
- Experience with Kafka, Kinesis, or other streaming platforms.
- Experience with CI/CD and DevOps practices.

Location: New York, NY (Hybrid)
Employment Type: Contract (12+ months)
Preferred: US Citizen or Green Card, but open to H1B.
"""

# Initialize session state
if "session_result" not in st.session_state:
    st.session_state.session_result = None
if "run_count" not in st.session_state:
    st.session_state.run_count = 0
if "all_pipeline_events" not in st.session_state:
    st.session_state.all_pipeline_events = []

st.title("AutoRecruit ADK – Multi-Agent Recruiting Copilot")
st.caption("Enterprise Agents Track • Google Agents Intensive Capstone Project")

st.markdown(
    """
Paste a job description, click **Run AutoRecruit**, and the multi-agent system will:
1. Parse the job description into a structured profile  
2. Search for top candidates from the synthetic database  
3. (Stub) Screen candidates  
4. Generate personalized outreach emails  
5. Log pipeline events for observability  
"""
)

# --- Layout ---
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("Job Description Input")
    # Use session state to maintain the text area value across reruns
    job_description = st.text_area(
        "Paste or edit the job description here:",
        value=st.session_state.get("job_description_value", default_jd),
        height=400,
        key="job_description_input"
    )
    
    # CRITICAL: Update session state AFTER the text area is rendered
    # This captures any edits the user made
    if job_description != st.session_state.get("job_description_value"):
        st.session_state.job_description_value = job_description

    if st.button("🚀 Run AutoRecruit"):
        # Get the CURRENT value from the text area widget (via session state key)
        current_job_description = st.session_state.job_description_input
        
        if not current_job_description.strip():
            st.error("Please paste a job description before running.")
        else:
            st.success("Running AutoRecruit pipeline…")
            session = run_recruiting_session(current_job_description)
            st.session_state.session_result = session
            
            # Append new events to the accumulated list (don't clear)
            st.session_state.all_pipeline_events.extend(pipeline_events)

with right_col:
    st.subheader("Run Settings")
    st.markdown(
        """
**Note:**  
This demo uses:
- Synthetic candidate data (`data/processed/candidates.csv`)
- A stubbed JobIntakeAgent & ScreeningAgent in the current bootstrap
- The real orchestration & tools structure
"""
    )


# --- Run pipeline results ---
if st.session_state.session_result:
    session = st.session_state.session_result

    # --- Show results in tabs ---
    tab_profile, tab_candidates, tab_emails, tab_logs = st.tabs(
        ["Job Profile", "Candidates", "Outreach Emails", "Pipeline Logs"]
    )

    # Job profile
    with tab_profile:
        st.subheader("Parsed Job Profile (from agents / stub)")
        if session.job_profile:
            st.json(session.job_profile)
        else:
            st.info("No job profile available (JobIntakeAgent not implemented yet).")

    # Candidates
    with tab_candidates:
        st.subheader("Top Candidate Matches")
        if session.candidate_list:
            candidates_df = pd.DataFrame(session.candidate_list)
            st.dataframe(candidates_df)
        else:
            st.info("No candidates returned.")

    # Emails
    with tab_emails:
        st.subheader("Generated Outreach Emails")
        if session.outreach_emails:
            for email in session.outreach_emails:
                with st.expander(
                    f"Email to {email.get('candidate_name', 'Unknown Candidate')} "
                    f"({email.get('candidate_id', '')})"
                ):
                    st.text(email.get("email_text", ""))
        else:
            st.info("No emails generated.")

    # Logs / Observability
    with tab_logs:
        st.subheader("Pipeline Logs (Observability)")  
        if st.session_state.all_pipeline_events:
            logs_df = pd.DataFrame(st.session_state.all_pipeline_events)
            st.dataframe(logs_df)
        else:
            st.info("No pipeline events logged yet.")
else:
    st.info("Paste a job description on the left and click **Run AutoRecruit** to see the system in action.")