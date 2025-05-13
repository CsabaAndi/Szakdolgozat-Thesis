import pandas as pd
import polars as pl
import streamlit as st
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

RAW_MAIN = Path("../../Data/datasets/football-data-co-uk/Raw-Data/Main-Leagues")
RAW_EXTRA = Path("../../Data/datasets/football-data-co-uk/Raw-Data/Extra-Leagues")
CLEANED_MAIN = RAW_MAIN.parents[1] / "Cleaned-Data" / RAW_MAIN.name
CLEANED_EXTRA = RAW_EXTRA.parents[1] / "Cleaned-Data" / RAW_EXTRA.name
COMBINED_DIR = CLEANED_MAIN / "seasons_combined"


def read_csv_safely(path):
    try:
        return pl.read_csv(path)
    except Exception as e:
        st.error(f"Failed to read {path}: {e}")
        return None


def extract_country_from_path(path, base_dir):
    parts = path.relative_to(base_dir).parts
    return parts[1] if len(parts) >= 3 else "Unknown"


def generate_all_in_one():
    all_csv_paths = list(COMBINED_DIR.glob("**/*.csv"))
    all_csv_paths = [
        path for path in all_csv_paths if path.name != "Seasons_leagues_combined.csv"
    ]
    if not all_csv_paths:
        st.warning("No CSV files found to combine.")
        return

    combined_df = pd.concat(
        (pd.read_csv(file) for file in all_csv_paths), ignore_index=True
    )
    combined_df = combined_df.dropna(axis=1, how="all")
    output_path = COMBINED_DIR / "Seasons_leagues_combined.csv"
    combined_df.to_csv(output_path, index=False)
    st.success(f"Combined Seasons & Leagues file saved at: {output_path}")


def generate_combined_seasons():
    COMBINED_DIR.mkdir(parents=True, exist_ok=True)
    league_files = defaultdict(lambda: defaultdict(list))

    for path in CLEANED_MAIN.glob("**/*.csv"):
        if "seasons_combined" in path.parts[-3:]:
            continue
        country = extract_country_from_path(path, CLEANED_MAIN)
        league_files[country][path.name].append(path)

    for country, leagues in league_files.items():
        for league_name, paths in leagues.items():
            with ThreadPoolExecutor() as executor:
                dfs = [
                    df for df in executor.map(read_csv_safely, paths) if df is not None
                ]
            if not dfs:
                continue

            all_cols = sorted({col for df in dfs for col in df.columns})
            dfs_std = [
                df.with_columns(
                    [pl.lit(None).alias(col) for col in set(all_cols) - set(df.columns)]
                ).select(all_cols)
                for df in dfs
            ]
            combined = pl.concat(dfs_std, how="vertical_relaxed")
            out_dir = COMBINED_DIR / country
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / league_name
            combined.write_csv(out_path)
            st.success(f"Saved: {out_path}")


def generate_combined_season_leagues():
    generate_combined_seasons()


if __name__ == "__main__":
    pass
