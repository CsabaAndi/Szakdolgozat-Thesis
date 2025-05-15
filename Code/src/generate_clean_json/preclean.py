import pandas as pd
import streamlit as st
from pathlib import Path


RAW_MAIN = Path("../../Data/datasets/football-data-co-uk/Raw-Data/Main-Leagues")
RAW_EXTRA = Path("../../Data/datasets/football-data-co-uk/Raw-Data/Extra-Leagues")
CLEANED_MAIN = RAW_MAIN.parents[1] / "Cleaned-Data" / RAW_MAIN.name
CLEANED_EXTRA = RAW_EXTRA.parents[1] / "Cleaned-Data" / RAW_EXTRA.name

def clean_csv_file(raw_path, clean_path):
    clean_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        df = pd.read_csv(raw_path, encoding="utf-8", low_memory=False)
        if "Date" in df.columns:
            df["Date"] = pd.to_datetime(
                df["Date"], format="mixed", dayfirst=True, errors="coerce"
            ).dt.date
            invalid_dates = df["Date"].isna().sum()
            if invalid_dates > 0:
                st.warning(f"{invalid_dates} unparsed date values in `{clean_path}`.")
        df.to_csv(clean_path, index=False)
        return clean_path
    except Exception as e:
        st.error(f"Failed cleaning `{raw_path}`\n{e}")
        return None

def clean_directory(raw_base, clean_base, exclude={"seasons_combined"}):
    for dirpath in raw_base.rglob("*"):
        if dirpath.is_dir() and dirpath.name in exclude:
            continue
        for file in dirpath.glob("*.csv"):
            raw_path = file
            rel_path = raw_path.relative_to(raw_base)
            clean_path = clean_base / rel_path
            cleaned = clean_csv_file(raw_path, clean_path)
            if cleaned:
                st.success(f"Cleaned: `{rel_path}`")

def clean_all():
    clean_directory(RAW_MAIN, CLEANED_MAIN)
    clean_directory(RAW_EXTRA, CLEANED_EXTRA)

def clean_all_main_league_csvs():
    clean_directory(RAW_MAIN, CLEANED_MAIN)

def clean_extra_league_csvs():
    clean_directory(RAW_EXTRA, CLEANED_EXTRA)


if __name__ == "__main__":
    pass
