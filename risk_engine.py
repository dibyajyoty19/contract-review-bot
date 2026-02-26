def normalize_severity(sev: str) -> str:
    sev = sev.lower()
    if "high" in sev:
        return "🔴 High"
    if "medium" in sev:
        return "🟠 Medium"
    return "🟢 Low"

def extract_risks(result: dict):
    final_risks = []

    for r in result.get("risks", []):
        final_risks.append({
            "type": r.get("type", "Other"),
            "severity": normalize_severity(r.get("severity", "Medium")),
            "evidence": r.get("evidence", "Not specified"),
            "explanation": r.get("explanation", "")
        })

    if not final_risks:
        final_risks.append({
            "type": "No Major Risks Detected",
            "severity": "🟢 Low",
            "evidence": "",
            "explanation": "The contract does not contain obvious high-risk clauses."
        })

    return final_risks