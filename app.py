
import streamlit as st

st.set_page_config(
    page_title="MedStudy AI",
    page_icon="🩺"
)

st.title("🩺 MedStudy AI")
st.subheader("Your MBBS Study Assistant")

st.write(
    "Welcome! Your medical AI website is starting here."
)

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

question = st.text_area(
    "Enter your medical question",
    placeholder="For example: Explain iron deficiency anemia"
)

if st.button("Submit Question"):
    if question.strip():
        st.write("Subject:", subject)
        st.write("Your question:", question)
        st.info(
            "Your interface works! Next, we'll connect "
            "the AI model so it can generate answers."
        )
    else:
        st.warning("Please enter a question.")
