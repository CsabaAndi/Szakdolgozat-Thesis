import streamlit as st
from translations.languages import translate


if "selected_language" not in st.session_state:
    st.session_state.selected_language = "en"


def pages():
    pages = {
        f"📘 {translate('sidebar_information_section_name')}": [
            st.Page(
                "pages/other/Welcome.py",
                title="▸ " + translate("main_page_sidebar_title"),
            ),
            st.Page(
                "pages/other/User_Manual.py",
                title="▸ " + translate("user_manual_sidebar_title"),
            ),
        ],
        f"🧲 {translate('sidebar_collecting_section_name')}": [
            st.Page(
                "pages/Data_Collection.py",
                title="▸ " + translate("data_collection_sidebar_title"),
            ),
        ],
        f"⚙️ {translate('sidebar_processing_section_name')}": [
            st.Page(
                "pages/Cleaning_Data.py",
                title="▸ " + translate("cleaning_generating_sidebar_title"),
            ),
            st.Page(
                "pages/File_Explorer.py",
                title="▸ " + translate("file_explorer_sidebar_title"),
            ),
        ],
        f"📊 {translate('sidebar_analysis_visualization_section_name')}": [
            st.Page(
                "pages/Sort_&_Filter_Match_History_Data.py",
                title="▸ " + translate("sort_filter_sidebar_title"),
            ),
            st.Page(
                "pages/Stats.py", title="▸ " + translate("statistics_sidebar_title")
            ),
        ],
        f"🤖 {translate('sidebar_ml_section_name')}": [
            st.Page(
                "pages/Machine_Learning.py",
                title="▸ " + translate("training_predictions_sidebar_title"),
            ),
        ],
    }

    with st.sidebar:
        st.markdown(f"", unsafe_allow_html=True)

    st.navigation(pages, expanded=True).run()
