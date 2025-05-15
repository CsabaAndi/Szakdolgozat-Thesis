import pandas as pd
import numpy as np
from datetime import datetime
import re


def sort_df_by_col_util(
    df: pd.DataFrame, col_to_sort: str, asc: bool = False
) -> pd.DataFrame:
    df = df.sort_values(by=[col_to_sort], ascending=asc)
    return df


def get_goals_util(df_score_col: pd.DataFrame) -> list:
    score = re.findall(r"\d+", str(df_score_col))
    return [int(score[0]), int(score[1])]


def create_goal_cols_util(
    df: pd.DataFrame,
    column_name: str = "Score",
) -> pd.DataFrame:

    df[["Goal_X", "Goal_Y"]] = df[column_name].apply(
        lambda x: pd.Series(get_goals_util(x))
    )
    df["all_goals"] = df["Goal_X"] + df["Goal_Y"]
    df["goal_diff"] = np.abs(df["Goal_X"] - df["Goal_Y"])

    return df


def calc_wdl_values(
    df_score_col: pd.DataFrame, df_team_x_col: pd.DataFrame, mcommon_team: str
) -> str:

    s1, s2 = get_goals_util(df_score_col)
    x, y = (s1, s2) if df_team_x_col == mcommon_team else (s2, s1)
    ret = "win" if x > y else "draw" if x == y else "lose"

    return ret


def filter_sort_df_by_date(
    df: pd.DataFrame,
    date_filter: bool,
    date_column: str = "Date",
    date_format: str = r"%d/%m/%Y",
    start_date: str = "01/01/1010",
    end_date: str = "01/01/2100",
    date_sort: bool = False,
    ascending: bool = False,
) -> pd.DataFrame:
    """Filters and sorts df between dates.

    Keyword arguments:
        df: DataFrame to filter and sort
        date_column: Column name of date in df
        date_format: Date format to use in start and end dates
        start_date: Start date (format: date_forma)
        end_date: End date (format: date_format)
        ascending: Sorting order (default: False, descending)


    Returns:
        filtered & sorted DataFrame
    """

    if date_filter:
        start = datetime.strptime(start_date, date_format).date()
        end = datetime.strptime(end_date, date_format).date()
        df = df.loc[df[date_column].between(start, end)]

    if date_sort:
        df = sort_df_by_col_util(df, date_column, asc=ascending)

    return df


def filter_df_by_col_value(
    df: pd.DataFrame,
    column_name: str = "League",
    filter: bool = False,
    filter_value: str = "win",
) -> pd.DataFrame:
    """Filters df Column based on value

    Keyword arguments:
        df: DataFrame to filter
        column_name: Column name (str)
        filter: boolean to use the filter
        filter_value: filter value (str)

    Returns:
        filtered DataFrame
    """

    if column_name == "Dev-team":
        return df

    if column_name == "Home & Away":
        return df[
            df["Home"].str.contains(filter_value, case=False, na=False)
            | df["Away"].str.contains(filter_value, case=False, na=False)
        ]

    if not filter:
        return df

    return df[df[column_name] == filter_value]


def filter_df_by_goals(
    df: pd.DataFrame,
    filter: bool = False,
    filter_mode: str = "all",
    all_g_between_low: int = 0,
    all_g_between_high: int = 100,
    x_g_between_low: int = 0,
    x_g_between_high: int = 100,
    y_g_between_low: int = 0,
    y_g_high: int = 100,
    sort_col: str = "all_goals",
    sort: bool = False,
    sort_asc: bool = True,
) -> pd.DataFrame:

    if filter:
        if filter_mode == "Sum Goals":
            df = df[df["all_goals"].between(all_g_between_low, all_g_between_high)]
        elif filter_mode == "Home Goals":
            df = df[df["Goal_X"].between(x_g_between_low, x_g_between_high)]
        elif filter_mode == "Away Goals":
            df = df[df["Goal_Y"].between(y_g_between_low, y_g_high)]

    if sort:
        match sort_col:
            case "Goal Sum":
                sort_col = "all_goals"
            case "Home":
                sort_col = "Goal_X"
            case "Away":
                sort_col = "Goal_Y"
            case "Goal Diff":
                sort_col = "goal_diff"
        df = sort_df_by_col_util(df, sort_col, asc=sort_asc)

    return df


if __name__ == "__main__":
    pass
