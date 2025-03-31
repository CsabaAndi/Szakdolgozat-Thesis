import streamlit as st
import os
import sys

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
    start_datanode = st.button(label="Start DataNode", type="secondary")
    terminate_datanode = st.button(label="Terminate DataNode", type="secondary")


if start_datanode:
    ws.run_datanode_app()


if terminate_datanode:
    ws.terminate_datanode_app()
    