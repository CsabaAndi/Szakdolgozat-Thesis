import learning.ml
import learning.ml.mltmp
import streamlit as st
import sys
import os
import generate_clean_json.generate_big_data as bigdata
import pandas as pd
import learning

# Add the path to the root folder to sys.path
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(root_path)

# Now you can import CONFIG
import debug_out
import file_loop.file_io as file_io
from CONFIG import Config

config = Config()

st.set_page_config(
    page_title="Tables",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

container = st.container(border=True)
col = st.columns((1.5, 4.5, 2), gap='medium')


with st.sidebar:
    all_country_button = st.button(label="ALL country test", type="secondary")
    start_mltmp = st.button(label="mltmp", type="secondary")
    scitest = st.button(label="sci", type="secondary")


if all_country_button:
    dat = pd.read_json(r"../output/data/processed/match-history/compressed/all_countries.json")
    #debug_out.print_df(dat)

    with st.container(border=True):
        st.markdown(f''':red[ Placeholder ]''')
        st.write(dat)


if start_mltmp:
    with st.container():
        with st.spinner('Please wait... Running the task'):
            learning.ml.mltmp.baseline()
    
if scitest:
    with st.container():
        with st.spinner('Please wait... Running the task'):
            learning.ml.mltmp.sckiittest()
