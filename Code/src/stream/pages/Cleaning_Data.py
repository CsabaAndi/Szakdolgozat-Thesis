import streamlit as st
import debug_out
from generate_clean_json import preclean, generate_big_data
from translations.languages import translate
from config_class import Config


config = Config()


with st.sidebar:
    gen_clean_main_league_button = st.button(
        label=translate("generate_clean_main_league_files"), type="secondary"
    )
    gen_clean_extra_league_button = st.button(
        label=translate("generate_clean_extra_league_files"), type="secondary"
    )
    gen_clean_big_csv_button = st.button(
        label=translate("generate_clean_combined_season_files"), type="secondary"
    )
    gen_clean_big_boss_button = st.button(
        label=translate("generate_clean_all_in_one_file"), type="secondary"
    )

if gen_clean_main_league_button:
    with debug_out.timed():
        preclean.clean_all_main_league_csvs()


if gen_clean_extra_league_button:
    with debug_out.timed():
        preclean.clean_extra_league_csvs()


if gen_clean_big_csv_button:
    with debug_out.timed():
        with st.spinner("🔄 Generating combined league files..."):
            generate_big_data.generate_combined_seasons()


if gen_clean_big_boss_button:
    with debug_out.timed():
        with st.spinner("🔄 Generating big boss..."):
            generate_big_data.generate_all_in_one()
