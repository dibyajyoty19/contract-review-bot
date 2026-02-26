import streamlit as st
from pdf_parser import extract_text_from_pdf
from analyzer import analyze_contract
from risk_engine import extract_risks

st.set_page_config("AI Contract Review Bot", layout="wide")

st.title("📄 AI Contract Review Bot")
st.caption("Understand legal contracts in plain English — instantly.")

uploaded = st.file_uploader("Upload Contract (PDF or TXT)", type=["pdf", "txt"])

contract_text = ""

if uploaded:
    if uploaded.type == "application/pdf":
        contract_text = extract_text_from_pdf(uploaded)
    else:
        contract_text = uploaded.read().decode("utf-8")

contract_text = st.text_area(
    "Or paste contract text here",
    value=contract_text,
    height=300
)

if st.button("🔍 Analyze Contract", use_container_width=True):
    if not contract_text.strip():
        st.error("Please provide contract text.")
    else:
        with st.spinner("Analyzing contract with AI..."):
            result = analyze_contract(contract_text)
            risks = extract_risks(result)

        st.success("Analysis completed")

        st.subheader("📌 Key Contract Details")
        st.json(result.get("key_details", {}))

        st.subheader("⚠️ Risk Analysis")
        for r in risks:
            with st.expander(f"{r['severity']} — {r['type']}"):
                st.markdown(f"**Why this matters:** {r['explanation']}")
                if r["evidence"]:
                    st.markdown("**Evidence from contract:**")
                    st.code(r["evidence"])

        st.subheader("🧠 Plain English Summary")
        st.write(result.get("summary", ""))

        st.subheader("📑 Clause Breakdown")
        for k, v in result.get("clauses", {}).items():
            st.markdown(f"**{k.replace('_',' ').title()}**")
            st.write(v)