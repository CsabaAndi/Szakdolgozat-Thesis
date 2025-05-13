import streamlit as st
import pandas as pd
import pyperclip
from pathlib import Path
from translations.languages import translate


def open_here_button(selected_csv, label):
    if st.button(label="Show Data Here", type="secondary"):
        df = pd.read_csv(selected_csv)
        with st.container(border=True):
            st.markdown(f""":red[{label}]""")
            st.write(df)


def copy_to_clipboard_button(selected_csv):
    if st.button(label="Copy to Clipboard", type="secondary"):
        pyperclip.copy(str(selected_csv))
        st.success("Copied to clipboard!")


def if_selected(label, selected_csv):
    show_file_result(label, selected_csv)
    copy_to_clipboard_button(selected_csv)
    open_here_button(selected_csv, label)


def get_csv_files_from_folder(folder_path: Path, nested=False):
    files = []
    if not folder_path.is_dir():
        return files

    try:
        for subfolder in folder_path.iterdir():
            if nested and subfolder.is_dir():
                for file in subfolder.glob("*.csv"):
                    league_name = format_league_name(file.name)
                    files.append((subfolder.name, league_name, file))
            elif not nested and subfolder.suffix == ".csv":
                league_name = format_league_name(subfolder.name)
                files.append(("", league_name, subfolder))
    except Exception as e:
        st.warning(f"Error reading folder: {folder_path}\n{e}")

    return files


def get_main_loop_files(base_path: Path):
    files = []
    if not base_path.is_dir():
        return files

    try:
        for season_folder in base_path.iterdir():
            if not season_folder.is_dir():
                continue
            for country_folder in season_folder.iterdir():
                if not country_folder.is_dir():
                    continue
                for file in country_folder.glob("*.csv"):
                    league_name = format_league_name(file.name)
                    files.append((season_folder.name, country_folder.name, league_name, file))
    except Exception as e:
        st.warning(f"Error reading folder: {base_path}\n{e}")

    return files


def format_league_name(file_name):
    return file_name.replace(".csv", "").replace("-", " ").title()


def show_file_result(label, file_path):
    st.write(f"**{translate('you_selected')}**: {label}")
    st.write(f"**{translate('file_path')}**: {file_path}")


st.title("File Explorer")

data_mode = st.radio("Select Data Mode", ["Raw Data", "Cleaned Data"], horizontal=True)

base_path = (
    Path("../../Data/datasets/football-data-co-uk/Raw-Data")
    if data_mode == "Raw Data"
    else Path("../../Data/datasets/football-data-co-uk/Cleaned-Data")
)

mode = st.radio("Select Mode", ["Main Leagues", "Extra Leagues"], horizontal=True)

options = ["Seasons"] if data_mode == "Raw Data" else ["Seasons", "Combined"]

if mode == "Main Leagues":
    submode = st.radio("Select Main Mode", options, horizontal=True)

    if submode == "Combined":
        combined_path = base_path / "Main-Leagues" / "seasons_combined"
        leagues = get_csv_files_from_folder(combined_path)

        league_dict = {league: path for _, league, path in leagues}
        selected_league = st.selectbox(translate("choose_league"), league_dict.keys())

        label = f"{data_mode} - Combined - {selected_league}"
        if_selected(label, league_dict[selected_league])

    elif submode == "Seasons":
        loop_path = base_path / "Main-Leagues"
        leagues = get_main_loop_files(loop_path)

        seasons = sorted(set(season for season, _, _, _ in leagues))
        selected_season = st.selectbox(translate("choose_season"), seasons)

        filtered_by_season = [
            (c, l, p) for s, c, l, p in leagues if s == selected_season
        ]
        countries = sorted(set(c for c, _, _ in filtered_by_season))
        selected_country = st.selectbox(translate("choose_country"), countries)

        filtered_by_country = [
            (l, p) for c, l, p in filtered_by_season if c == selected_country
        ]
        league_dict = {l: p for l, p in filtered_by_country}
        selected_league = st.selectbox(translate("choose_league"), league_dict.keys())

        label = (
            f"{data_mode} - {selected_season} - {selected_country} - {selected_league}"
        )
        if_selected(label, league_dict[selected_league])

elif mode == "Extra Leagues":
    extra_path = base_path / "Extra-Leagues"
    extra_leagues = get_csv_files_from_folder(extra_path, nested=True)

    countries = sorted(set(country for country, _, _ in extra_leagues))
    selected_country = st.selectbox(translate("choose_country"), countries)

    filtered_by_country = [(l, p) for c, l, p in extra_leagues if c == selected_country]
    league_dict = {l: p for l, p in filtered_by_country}
    selected_league = st.selectbox(translate("choose_league"), league_dict.keys())

    label = f"{data_mode} - {selected_country} - {selected_league}"
    if_selected(label, league_dict[selected_league])
