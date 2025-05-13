import streamlit as st
from ml import ml_stats
import controller.selectors as selectors
from config_class import Config


config = Config()


with st.sidebar:
    unique_combined, selected_country, league_path, _ = selectors.select()
    start_mltmp = st.button(label="Show statistics", type="secondary")

if start_mltmp:
    with st.container():
        with st.spinner("Please wait... Running the task"):
            ml_stats.base_stats(league_path)
