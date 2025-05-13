import pandas as pd
import data_man.data_utils as data_utils
import debug_out
from config_class import Config


def filter_and_sort_df(preclean_df: pd.DataFrame) -> pd.DataFrame:

    config = Config()
    Configuration = config.get_config_dict()
    most_common_team = Configuration["Side-team"]

    data_utils.create_goal_cols_util(df=preclean_df, column_name="Score")

    preclean_df["wdl"] = preclean_df.apply(
        lambda x: data_utils.calc_wdl_values(x["Score"], x["Home"], most_common_team),
        axis=1,
    )

    side_filtered_df = data_utils.filter_df_by_col_value(
        preclean_df,
        column_name=Configuration["Side-value"],
        filter=Configuration["Side-checkbox"],
        filter_value=Configuration["Side-team"],
    )

    league_types = "E0"
    league_filtered_df = data_utils.filter_df_by_col_value(
        side_filtered_df,
        column_name="League",
        filter=False,  # Configuration["League-checkbox"],
        filter_value=league_types[0],
    )

    goal_filtered_df = data_utils.filter_df_by_goals(
        league_filtered_df,
        filter=Configuration["Goal-checkbox"],
        filter_mode=Configuration["Goal-mode"],
        all_g_between_low=Configuration["Goal-between-all-low"],
        all_g_between_high=Configuration["Goal-between-all-high"],
        x_g_between_low=Configuration["Goal-between-x-low"],
        x_g_between_high=Configuration["Goal-between-x-high"],
        y_g_between_low=Configuration["Goal-between-y-low"],
        y_g_high=Configuration["Goal-between-y-high"],
        sort=Configuration["Goal-sort-checkbox"],
        sort_col=Configuration["Goal-sort-column"],
        sort_asc=Configuration["Goal-sort-order"],
    )

    wdl_filtered_df = data_utils.filter_df_by_col_value(
        goal_filtered_df,
        column_name="wdl",
        filter=Configuration["Wdl-checkbox"],
        filter_value=Configuration["Wdl-value"],
    )

    date_sorted_filtered_df = data_utils.filter_sort_df_by_date(
        wdl_filtered_df,
        date_filter=Configuration["Date-checkbox"],
        date_column="Date",
        date_format=Configuration["Date-start-end-format"],
        start_date=Configuration["Date-filter-start"],
        end_date=Configuration["Date-filter-end"],
        date_sort=Configuration["Date-sort"],
        ascending=Configuration["Date-sort-order"],
    )

    debug_out.print_df(date_sorted_filtered_df)

    return date_sorted_filtered_df


if __name__ == "__main__":
    pass
