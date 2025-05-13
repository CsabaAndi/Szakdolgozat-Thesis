import pandas as pd
import streamlit as st
from pathlib import Path


def select():
    base_path = Path("../../Data/datasets/football-data-co-uk/Cleaned-Data/Main-Leagues/seasons_combined/").resolve()

    countries = sorted([folder.name for folder in base_path.iterdir() if folder.is_dir()])

    selected_country = st.selectbox("Select Country", countries)
    country_path = base_path / selected_country

    leagues = sorted([file.name for file in country_path.iterdir() if file.suffix == ".csv"])
    league_display_names = [file.stem for file in country_path.iterdir() if file.suffix == ".csv"]

    selected_league_display = st.selectbox("Select League", league_display_names)
    selected_league = f"{selected_league_display}.csv"
    league_path = country_path / selected_league

    df = pd.read_csv(league_path, usecols=["HomeTeam", "AwayTeam"])
    unique_combined = pd.unique(df[["HomeTeam", "AwayTeam"]].dropna().values.ravel())

    return unique_combined, selected_country, str(league_path), selected_league_display
