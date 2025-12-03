# 🏆 AutoRecruit ADK

## A Multi-Agent Recruiting Copilot for End-to-End Hiring

**Enterprise Agents Track – Google Agents Intensive Capstone Project**

---

## 📌 Overview

AutoRecruit ADK is a multi-agent enterprise recruiting copilot built using Google's Agent Development Kit (ADK). It automates the entire IT recruiting workflow:

- Job intake and profile extraction
- Intelligent candidate search and matching
- Profile screening and evaluation
- Personalized outreach email generation
- Pipeline logging and observability

This project demonstrates how AI agents can automate real-world business workflows in staffing and recruiting.

---

## ✨ Key Features

- ✅ End-to-end automation of the hiring pipeline
- ✅ Modular multi-agent system
- ✅ Dynamic job description parsing
- ✅ Custom candidate search tool
- ✅ Personalized outreach emails generated automatically
- ✅ Full pipeline observability with logging
- ✅ Interactive Streamlit web interface
- ✅ Session memory and state management

---

## 🚀 Getting Started

### Installation

```bash
git clone https://github.com/KishoreKu/autorecruit-adk.git
cd autorecruit-adk
pip install -r requirements.txt
```

### Run the Web Demo

```bash
streamlit run scripts/web_demo.py
```

Visit `http://localhost:8501` in your browser.

---

## 🏗️ Architecture

```
Job Description Input
    ↓
JobIntakeAgent (Parse & Extract)
    ↓
CandidateSourcingAgent (Search)
    ↓
CandidateScreeningAgent (Evaluate)
    ↓
OutreachAgent (Generate Emails)
    ↓
Pipeline Logger (Observability)
```

---

## 🎯 ADK Concepts Demonstrated

✅ Multi-Agent Systems  
✅ Sequential & Parallel Agents  
✅ Custom Tools  
✅ Session Memory  
✅ Observability & Logging  
✅ Agent Evaluation  

---

## 📁 Project Structure

```
src/autorecruit/
├── agents/               # Multi-agent system
│   ├── job_intake_agent.py
│   ├── candidate_sourcing_agent.py
│   ├── candidate_screening_agent.py
│   ├── outreach_agent.py
│   └── orchestrator_agent.py
├── tools/                # Custom tools
│   ├── candidate_search_tool.py
│   ├── email_template_tool.py
│   └── pipeline_logger_tool.py
├── memory/               # Session management
│   └── session_memory.py
└── app/
    └── run_recruiting_session.py

scripts/
├── run_demo.py           # CLI demo
└── web_demo.py           # Streamlit web interface

data/
└── processed/candidates.csv   # Synthetic candidate database
```

---

## 💡 How It Works

1. **Paste a job description** in the web interface
2. **Job Profile extracted** - Title, location, skills, experience level
3. **Candidates sourced** - Top matches from database
4. **Emails generated** - Personalized outreach for each candidate
5. **Pipeline logged** - Full execution trace with timestamps

---

## 🔮 Future Work

- ATS integration (Greenhouse, Lever, etc.)
- Vector DB for semantic matching
- SMS/WhatsApp outreach
- Interview scheduling
- Recruiter dashboard

---

## 📝 License

MIT License

---

## 👤 Author

**Kishore Alajangi**  
Built with ❤️ using Google ADK
