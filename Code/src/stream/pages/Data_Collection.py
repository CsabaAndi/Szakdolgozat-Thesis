import streamlit as st
import threading
import webscrape_start as webscrape
from translations.languages import translate


st.header(translate("legal_notice_title"))
st.markdown(translate("legal_notice_body"), unsafe_allow_html=True)
st.header(translate("legal_note_title"))
st.markdown(translate("legal_note_body"), unsafe_allow_html=True)

with st.sidebar:
    st.header("Demo:")
    start_ws = st.button(
        label=translate("webscraper_run_button"), type="secondary"
    )
    terminate_ws = st.button(
        label=translate("webscraper_terminate_button"), type="secondary"
    )


if start_ws:
    with st.spinner("Running the task..."):
        task_thread = threading.Thread(target=webscrape.run_ws_demo())
        task_thread.start()
        task_thread.join()
    st.success(
        'Demo Completed!'
    )


if terminate_ws:
    with st.spinner("Terminatig DataNode Process..."):
        webscrape.terminate_ws_demo()
    st.success("Demo Terminated!")
