import pandas as pd
import streamlit as st
import plotly.express as px
import data_man.data_adapter as data_adapter
import stats.filter_and_sort_df as stats_filter_sort
from stream.translations.languages import translate
from config_class import Config

pd.options.plotting.backend = "plotly"


config = Config()
config.set_side_team("Arsenal")
config.set_config_dict(
    {
        "Side-checkbox": False,
        "Side-value": "All ",
        "Side-team": "Arsenal",
        "League-checkbox": False,
        "Wdl-checkbox": False,
        "Wdl-value": "Win",
        "Goal-checkbox": False,
        "Goal-mode": "between",
        "Goal-between-all-low": 0,
        "Goal-between-all-high": 100,
        "Goal-between-x-low": 0,
        "Goal-between-x-high": 100,
        "Goal-between-y-low": 0,
        "Goal-between-y-high": 100,
        "Goal-sort-checkbox": False,
        "Goal-sort-column": "goals_sum",
        "Goal-sort-order": "Ascending",
        "Date-checkbox": False,
        "Date-start-end-format": r"%d/%m/%Y",
        "Date-sort": False,
        "Date-filter-start": "",
        "Date-filter-end": "",
        "Date-sort-order": "Ascending",
    }
)


def base_stats(path):
    filtered_sorted_df = stats_filter_sort.filter_and_sort_df(
        data_adapter.adapt(path, extended_ml_model=True)
    )
    df = filtered_sorted_df.drop(columns=["wdl", "Goal_X", "Goal_Y"], errors="ignore")
    df = df.rename(columns={"all_goals": "goals_sum"})

    correct_preds = df["FTR"].isin(["H", "D"]).sum()
    false_accuracy = correct_preds / len(df)

    cols_to_analyze = ["FTHG", "FTAG", "goals_sum", "B365H", "B365D", "B365A"]

    with st.container(border=True):
        highlight_style = "color:green; font-weight:bold;"

        st.subheader(translate("ml_stats_subheader_datsample"))
        st.write(df.head(15))

        st.subheader(translate("ml_stats_subheader_distribution"))
        st.write(df["FTR"].value_counts())
        st.markdown(
            f"{translate("ml_stats_falseacc")} <span style='{highlight_style}'>{false_accuracy:.2%}</span>",
            unsafe_allow_html=True,
        )

        st.subheader(translate("ml_stats_subheader_describe"))
        st.write(df[cols_to_analyze].describe())

        for col in cols_to_analyze:
            st.subheader(f"{translate("ml_stats_subheader_statistics")} [{col}]")

            stats = {
                translate("ml_stats_min"): df[col].min(),
                translate("ml_stats_max"): df[col].max(),
                translate("ml_stats_avg"): df[col].mean(),
                translate("ml_stats_med"): df[col].median(),
                translate("ml_stats_std"): df[col].std(),
            }

            for stat_name, stat_value in stats.items():
                st.markdown(
                    f"{stat_name}: <span style='{highlight_style}'>{stat_value:.8f}</span>",
                    unsafe_allow_html=True,
                )

            fig = px.histogram(
                df, x=col, nbins=30, title=f"{col} {translate("ml_stats_dist")}"
            )
            st.plotly_chart(fig)
            st.write("---")


if __name__ == "main":
    pass
