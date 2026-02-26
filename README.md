# 📄 AI Contract & Document Review Bot

An AI-powered tool that analyzes legal contracts and presents a clear, structured summary in plain English — helping non-lawyers understand key clauses and risks quickly.

Built as part of an **AI Automation Engineer – Fresher Hiring Task**.

---

## 🚀 Features

- 📂 Upload contracts as **PDF** or paste raw text
- 🧠 AI-powered analysis using **LLM (Gemini-ready, LLM-agnostic)**
- 📌 Extracts key details:
  - Parties involved
  - Contract duration
  - Payment terms
- ⚠️ Risk flagging with severity levels:
  - Auto-renewal clauses
  - Liability risks
  - Missing exit clauses
- 🧾 Plain-English summary for business users
- 📑 Structured output (not a wall of text)
- 🛡️ Graceful fallback demo mode for quota-limited APIs

---

## 🧠 Architecture Overview
User → Streamlit UI → Contract Parser → LLM Analyzer → Risk Engine → Structured Report


The system is **LLM-agnostic**.  
Only the `analyzer.py` module changes when switching between Claude / Gemini / OpenAI.

---

## 📁 Project Structure
contract-review-bot/
├── app.py # Streamlit UI & main flow
├── analyzer.py # LLM prompt + response parsing
├── pdf_parser.py # PDF → text extraction
├── risk_engine.py # Risk severity normalization
├── mock_response.py # Demo fallback response
├── requirements.txt
├── .env.example
├── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd contract-review-bot

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py