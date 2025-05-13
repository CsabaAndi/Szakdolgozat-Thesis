import streamlit as st
from translations.languages import translate


languages = ["en", "hu"]

if "selected_language" not in st.session_state:
    st.session_state.selected_language = "en"

st.markdown(
    f"""
    <h1 style="margin-bottom: 0.5em;">{translate("thesis_title")}</h1>
    <p><strong>{translate("thesis_author")}:</strong> {translate("thesis_author_value")}</p>
    <p><strong>{translate("thesis_supervisor")}:</strong> {translate("thesis_supervisor_value")}</p>
    <p><strong>{translate("thesis_university")}:</strong> {translate("thesis_university_value")}</p>
    <p><strong>{translate("thesis_year")}:</strong> 2025</p>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown(f"<br>", unsafe_allow_html=True)
    st.session_state.selected_language = st.selectbox(
        label=translate("select_language"),
        options=languages,
        index=languages.index(st.session_state.selected_language),
        key=645456456465,
    )
