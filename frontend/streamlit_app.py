import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

# Session state

if "report" not in st.session_state:
    st.session_state.report = ""

if "follow_up_answer" not in st.session_state:
    st.session_state.follow_up_answer = ""

st.title("Deep Research Agent")

# -----------------------------

# Main Research Query

# -----------------------------

topic = st.text_input("Research Topic")

if st.button("Research"):
    with st.spinner("Researching..."):
        try:
            response = requests.post(
                f"{BACKEND_URL}/full_research",
                json={"query": topic},
                timeout=1000
            )
            result = response.json()

            # Store report for later follow-up/export
            if "report" in result:
                st.session_state.report = result["report"]

            # Research Plan
            st.subheader("Research Plan")
            if result.get("plan"):
                st.write(result["plan"])
            else:
                st.error("Failed to retrieve a research plan.")

            # URLs
            if result.get("urls"):
                st.subheader("Found URLs")
                st.write(result["urls"])

            # Notes
            if result.get("notes"):
                st.subheader("Summary Notes")
                st.write(result["notes"])

            # Errors
            if result.get("error"):
                st.error(result["error"])

            # Report
            if result.get("report"):
                st.subheader("Research Report")
                st.markdown(result["report"])
        except Exception as e:
            st.error(f"Research failed: {str(e)}")

# -----------------------------

# Download Section

# -----------------------------

if st.session_state.report:
    st.divider()
    st.subheader("Download Report")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.download_button(
            label="Download Markdown",
            data=st.session_state.report,
            file_name="research_report.md",
            mime="text/markdown"
        )
    with col2:
        if st.button("Generate DOCX"):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/export_docx",
                    json={"report": st.session_state.report}
                )
                st.download_button(
                    label="Download DOCX",
                    data=response.content,
                    file_name="research_report.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
            except Exception as e:
                st.error(f"DOCX generation failed: {str(e)}")
    with col3:
        if st.button("Generate PDF"):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/export_pdf",
                    json={"report": st.session_state.report}
                )
                st.download_button(
                    label="Download PDF",
                    data=response.content,
                    file_name="research_report.pdf",
                    mime="application/pdf"
                )
            except Exception as e:
                st.error(f"PDF generation failed: {str(e)}")

# -----------------------------

# Follow-up Questions

# -----------------------------

if st.session_state.report:
    st.divider()
    st.subheader("Follow-up Research")
    follow_up = st.text_input("Ask a follow-up question")
    if st.button("Continue Research"):
        if not follow_up.strip():
            st.warning("Please enter a follow-up question.")
        else:
            try:
                response = requests.post(
                    f"{BACKEND_URL}/follow_up",
                    json={"report": st.session_state.report, "question": follow_up}
                )
                answer = response.json().get("answer", "No response received.")
                st.session_state.follow_up_answer = answer
            except Exception as e:
                st.error(f"Follow-up failed: {str(e)}")
    if st.session_state.follow_up_answer:
        st.subheader("Follow-up Answer")
        st.markdown(st.session_state.follow_up_answer)
