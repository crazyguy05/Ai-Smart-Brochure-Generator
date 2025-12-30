import streamlit as st
from brochure_Generator import create_brochure, stream_brochure_streamlit




# =========================
# Streamlit UI
# =========================

st.set_page_config(
    page_title="AI Smart Brochure Generator",
    layout="centered"
)

st.title("AI Smart Brochure Generator")
st.write("Generate a company brochure using a local LLM (Ollama) and website data.")

company_name = st.text_input("Company Name")
url = st.text_input("Company Website URL")

if st.button("Generate Brochure"):

    if not company_name or not url:
        st.warning("Please enter both company name and website URL.")
        st.stop()

    with st.spinner("Generating brochure... This may take a moment"):
        try:
            brochure = stream_brochure_streamlit(company_name, url)

        except Exception as e:
            st.error("Something went wrong while generating the brochure.")
            st.code(str(e))
            st.stop()

    if not brochure or len(brochure.strip()) == 0:
        st.error("The AI returned an empty brochure. Try again.")
        st.stop()

    # Display brochure
    st.markdown(brochure)

