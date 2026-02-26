import os
import json
import re
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found in .env")

genai.configure(api_key=API_KEY)

# ✅ CORRECT MODEL FOR v1beta
model = genai.GenerativeModel("models/gemini-pro-latest")

SYSTEM_PROMPT = """
You are a senior legal analyst AI assisting non-lawyers.

Analyze the given contract and return ONLY valid JSON.
Do not include markdown or explanations.

Follow this EXACT JSON schema:

{
  "key_details": {
    "parties": "string",
    "effective_date": "string",
    "contract_duration": "string",
    "payment_terms": "string"
  },
  "clauses": {
    "termination": "string",
    "renewal": "string",
    "liability": "string",
    "confidentiality": "string",
    "intellectual_property": "string"
  },
  "risks": [
    {
      "type": "Auto-Renewal | Liability | Missing Termination | IP Ownership | Other",
      "severity": "Low | Medium | High",
      "evidence": "Exact sentence(s) from the contract",
      "explanation": "Plain English explanation"
    }
  ],
  "summary": "Plain English business summary"
}
"""

def clean_json(text: str) -> str:
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group(0) if match else text

def analyze_contract(contract_text: str) -> dict:
    prompt = SYSTEM_PROMPT + "\n\nCONTRACT:\n" + contract_text[:12000]
    response = model.generate_content(prompt)

    cleaned = clean_json(response.text)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {
            "key_details": {},
            "clauses": {},
            "risks": [],
            "summary": "⚠️ AI response could not be parsed."
        }