import streamlit as st
import os
import sys
import threading

# Add the path to the root folder to sys.path
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(root_path)

# Now you can import CONFIG
import debug_out
import webscrape_start as ws

st.set_page_config(
    page_title="DataNode",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

container = st.container(border=True)
col = st.columns((1.5, 4.5, 2), gap='medium')


with st.sidebar:
    # Buttons
    side_loop_cb = st.checkbox(label="Loop through all")
    side_mh_tpage = st.number_input(label="Match history x pages back", min_value=0, max_value=100, value=0, step=1, key=10000000000000000000)
    start_datanode = st.button(label="Start DataNode", type="secondary")
    terminate_datanode = st.button(label="Terminate DataNode", type="secondary")


if start_datanode:
    with st.spinner('Running the task...'):
        task_thread = threading.Thread(target=ws.run_datanode_app(arg_loop=bool(side_loop_cb), arg_page=side_mh_tpage))
        task_thread.start()
        task_thread.join()
    st.success('Task completed! - Data saved to "Code/cakdoga/output/data/preprocessed" Folder!')


if terminate_datanode:
    with st.spinner('Terminatig DataNode Process...'):
        ws.terminate_datanode_app()
    st.success('Terminated DataNode Process!')
    