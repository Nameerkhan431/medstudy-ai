
import os
import streamlit as st
from google import genai

st.set_page_config(
    page_title="MedStudy AI",
    page_icon="🩺"
)

st.title("🩺 MedStudy AI")
st.subheader("Your MBBS Study Assistant")

st.info(
    "For educational use only. Verify medical facts "
    "against trusted textbooks and current guidelines."
)

# Get your secret API key securely
try:
    api_key = st.secrets.get("GEMINI_API_KEY", "")
except Exception:
    api_key = ""

api_key = api_key or os.getenv("GEMINI_API_KEY", "")

if not api_key:
    st.error(
        "Gemini API key is not configured. "
        "Add GEMINI_API_KEY in Streamlit Secrets."
    )
    st.stop()

client = genai.Client(api_key=api_key)

subject = st.selectbox(
    "Choose your MBBS subject",
    [
        "Pathology",
        "Pharmacology",
        "Medicine",
        "Surgery",
        "Anatomy",
        "Physiology",
        "Biochemistry",
        "Community Medicine",
        "ENT",
        "Ophthalmology"
    ]
)

mode = st.selectbox(
    "Choose study mode",
    [
        "Explain a topic",
        "Viva questions",
        "Generate MCQs",
        "Summarize a topic"
    ]
)

question = st.text_area(
    "Enter your medical question",
    placeholder="For example: Explain iron deficiency anemia"
)

if st.button("Generate Answer"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        prompt = f"""
You are MedStudy AI, an educational assistant for MBBS students.

Subject: {subject}
Study mode: {mode}
Student's request: {question}

Instructions:
- Give a clear, structured MBBS-level answer.
- Use headings and bullet points.
- For viva questions, include answers.
- For MCQs, provide four options, one best answer,
  and an explanation.
- Never invent medical references.
- Mention uncertainty where appropriate.
- Encourage checking trusted textbooks and current
  clinical guidelines.
- Do not replace professional medical care.
"""

        with st.spinner("Gemini is preparing your answer..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                if response.text:
                    st.markdown("## Answer")
                    st.markdown(response.text)
                else:
                    st.warning("No answer returned. Please try again.")

            except Exception as e:
                st.error(
                    "The AI request failed. Check your API key, "
                    "model availability, and API quota."
                )
                st.caption(str(e))
