import pandas as pd


def adapt(path_to_csv, extended_ml_model=False):

    base_columns = ["Date", "Div", "HomeTeam", "AwayTeam", "FTHG", "FTAG"]
    ml_extra_columns = ["FTR", "B365H", "B365D", "B365A"]
    selected_columns = (
        base_columns + ml_extra_columns if extended_ml_model else base_columns
    )

    df = pd.read_csv(path_to_csv, usecols=selected_columns)

    df = df.drop_duplicates()

    dropna_columns = ["FTHG", "FTAG"]
    if extended_ml_model:
        dropna_columns += ["FTR", "B365H", "B365D", "B365A"]

    df = df.dropna(subset=dropna_columns)
    df.fillna(-1, inplace=True)
    df[["FTHG", "FTAG"]] = df[["FTHG", "FTAG"]].astype(int)
    df["Score"] = df["FTHG"].astype(str) + "-" + df["FTAG"].astype(str)
    df.rename(columns={"HomeTeam": "Home", "AwayTeam": "Away"}, inplace=True)
    df["Date"] = pd.to_datetime(
        df["Date"], dayfirst=True, format="mixed", errors="coerce"
    ).dt.date

    return df
