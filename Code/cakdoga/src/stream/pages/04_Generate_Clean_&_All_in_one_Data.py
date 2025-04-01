import streamlit as st
import sys
import os
import generate_clean_json.generate_big_data as bigdata
import pandas as pd

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
    # Buttons
    gen_clean_mh_button = st.button(label="Generate clean match history json files", type="secondary")
    gen_clean_big_mh_button = st.button(label="Generate clean all-in one match history json file", type="secondary")
    
    table_rb = st.radio(label="Which Table to use in generating", options=["Last", "Ou","Player", "Wide"], horizontal=True, key=222222222222)
    gen_big_tables_button = st.button(label="Generate clean all-in one table json file", type="secondary")
    mh_all = st.button(label="Show all MH", type="secondary")
    t_all = st.button(label="Show all Table", type="secondary")


if gen_clean_mh_button:
    
    config.set_mode("Data")
    with debug_out.timed():
        file_io.read_all_files_in_dir(st)
    
    
if gen_clean_big_mh_button:
    
    config.set_mode("Data???")
    with debug_out.timed():
        bigdata.generate_mh_big_data()
    #file_io.read_all_files_in_dir(st)

if gen_big_tables_button:
    config.set_mode("Data???")
    config.set_table_type(table_rb)

    with debug_out.timed():
        bigdata.generate_tables_big_data(config)
    #file_io.read_all_files_in_dir(st)
    
if mh_all:
    dat = pd.read_json(r"../output/data/processed/match-history/compressed/all_countries.json")
    dat['Date'] = pd.to_datetime(dat['Date'], format=r'%d/%m/%y').dt.date
    debug_out.print_df(dat)

    with st.container(border=True):
        st.markdown(f''':red[ Match-History All-in-One ]''')
        st.write(dat)

if t_all:
    dat = pd.read_json(r"../output/data/processed/tables/compressed/all_tables_Wide.json")
    debug_out.print_df(dat)

    with st.container(border=True):
        st.markdown(f''':red[ All-in-One ]''')
        st.write(dat)
    