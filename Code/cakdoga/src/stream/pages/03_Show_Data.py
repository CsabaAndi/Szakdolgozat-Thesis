import streamlit as st
import sys
import os


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
    # tables
    table_rb = st.radio(label="Which Table", options=["Last", "Ou","Player", "Wide"], horizontal=True, key=222)
    
    
    # Buttons
    reset_button = st.button(label="Reset", on_click=None, type="primary")
    progi_button = st.button(label="Start", type="secondary")
    configout_button = st.button(label="Configout", type="secondary")
    


if progi_button:
    
    # Initialize config objects
    #GUI_mode_Config = CONFIG.ModeConfig("MatchHistory")
    #GUI_Match_History_Config = CONFIG.MatchHistoryConfig(config_dict=handle_configout_click())
    
    # TODO: na ez aszért bad mert init után lesz mindig értéke és ha van értlke akk rosszul hivpodik a match case mostan ibad !!!!!!!
    # ezé itt ""
    #GUI_table_type_Config = CONFIG.TableTypeConfig("")
    
    config.set_mode("Tables")
    config.set_table_type(table_rb)
    
    with debug_out.timed():
            file_io.read_all_files_in_dir(st)
    

if configout_button:
    with col[0]:
        container.write(config.get_table_type())



if reset_button:
    with col[2]:
        container.write("Placeholder")