import streamlit as st
import sidebar_navigation


def main():
    st.set_page_config(layout="wide")
    if "selected_language" not in st.session_state:
        st.session_state.selected_language = "en"
    sidebar_navigation.pages()


if __name__ == "__main__":
    main()
