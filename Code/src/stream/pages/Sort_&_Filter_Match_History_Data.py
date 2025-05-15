import streamlit as st
import debug_out
import data_man.data_adapter as data_adapter
import stats.filter_and_sort_df as stats_filter_sort
from controller import selectors, modes_controller
from config_class import Config


config = Config()

container = st.container(border=True)
col = st.columns((1.5, 4.5, 2), gap="medium")

def handle_configout_click(show=False):
    selected_values = {
        "Side-checkbox": bool(side_filter_cb),
        "Side-value": side_rb,
        "Side-team": side_team,
        "League-checkbox": False,  # bool(league_filter_cb),
        "Wdl-checkbox": bool(wdl_filter_cb),
        "Wdl-value": wdl_rb,
        "Goal-checkbox": bool(goal_filter_cb),
        "Goal-mode": bound_rb,
        "Goal-between-all-low": all_min_bi,
        "Goal-between-all-high": all_max_bi,
        "Goal-between-x-low": x_min_bi,
        "Goal-between-x-high": x_max_bi,
        "Goal-between-y-low": y_min_bi,
        "Goal-between-y-high": y_max_bi,
        "Goal-sort-checkbox": bool(goal_sort_cb),
        "Goal-sort-column": goal_sort_col_rb,
        "Goal-sort-order": goal_asc_rb == "Ascending",
        "Date-checkbox": bool(date_filter_cb),
        "Date-start-end-format": r"%d/%m/%Y",
        "Date-sort": bool(date_sort_cb),
        "Date-filter-start": start_date_dp.strftime("%d/%m/%Y"),
        "Date-filter-end": end_date_dp.strftime("%d/%m/%Y"),
        "Date-sort-order": date_asc_rb == "Ascending",
    }
    
    if show:
        with col[1]:
            container.write("### Selected Values:")
            for key, value in selected_values.items():
                container.write(f"- {key}: {value}")

    return selected_values


with st.sidebar:
    st.header("Sort & Filter Cleaned Data")
    unique_combined, selected_country, league_path, selected_league_display = (
        selectors.select()
    )

    loop_cb = st.checkbox(label="Loop through all teams")
    side_team = st.selectbox(
        "Select a team", unique_combined, index=0, key=4564564, disabled=loop_cb
    )

    side_filter_cb = st.checkbox(label="Side filter")
    side_rb = st.radio(
        label="Side Filter Values",
        options=["Home & Away", "Home", "Away"],
        horizontal=True,
        key=1,
        disabled=not side_filter_cb,
    )

    # League filter
    # league_filter_cb = st.checkbox(label="League filter")

    wdl_filter_cb = st.checkbox(label="WDL filter")
    wdl_rb = st.radio(
        label="WDL Filter Values",
        options=["win", "draw", "lose"],
        horizontal=True,
        key=2,
        disabled=not wdl_filter_cb,
    )

    goal_filter_cb = st.checkbox(label="Goal filter")
    bound_rb = st.radio(
        label="Goal Filter Values",
        options=["Sum Goals", "Home Goals", "Away Goals"],
        horizontal=True,
        key=3,
        disabled=not goal_filter_cb,
    )

    all_min_bi = st.number_input(
        label="Sum - minimum",
        min_value=0,
        max_value=100,
        value=0,
        step=1,
        key=100,
        disabled=not goal_filter_cb,
    )

    all_max_bi = st.number_input(
        label="Sum - maximum",
        min_value=0,
        max_value=100,
        value=100,
        step=1,
        key=150,
        disabled=not goal_filter_cb,
    )

    x_min_bi = st.number_input(
        label="Home - minimum",
        min_value=0,
        max_value=100,
        value=0,
        step=1,
        key=200,
        disabled=not goal_filter_cb,
    )

    x_max_bi = st.number_input(
        label="Home - maximum",
        min_value=0,
        max_value=100,
        value=100,
        step=1,
        key=250,
        disabled=not goal_filter_cb,
    )

    y_min_bi = st.number_input(
        label="Away - minimum",
        min_value=0,
        max_value=100,
        value=0,
        step=1,
        key=300,
        disabled=not goal_filter_cb,
    )

    y_max_bi = st.number_input(
        label="Away - maximum",
        min_value=0,
        max_value=100,
        value=100,
        step=1,
        key=350,
        disabled=not goal_filter_cb,
    )

    goal_sort_cb = st.checkbox(label="Goal Sort")
    goal_sort_col_rb = st.radio(
        label="Sort by ... goals",
        options=["Goal Sum", "Goal Diff", "Home", "Away"],
        horizontal=True,
        key=500,
        disabled=not goal_sort_cb,
    )

    goal_asc_rb = st.radio(
        label="Goal Sort asc/desc",
        options=["Ascending", "Descending"],
        horizontal=True,
        key=4,
        disabled=not goal_sort_cb,
    )

    date_filter_cb = st.checkbox(label="Date Filter")
    start_date_dp = st.date_input(
        label="Date-start",
        value="today",
        format="DD/MM/YYYY",
        key=10,
        disabled=not date_filter_cb,
    )

    end_date_dp = st.date_input(
        label="Date-end",
        value="today",
        format="DD/MM/YYYY",
        key=20,
        disabled=not date_filter_cb,
    )

    date_sort_cb = st.checkbox(label="Date Sort")
    date_asc_rb = st.radio(
        label="Date Sort asc/desc",
        options=["Ascending", "Descending"],
        horizontal=True,
        key=5,
        disabled=not date_sort_cb,
    )

    debug_cb = st.checkbox(label="(dev) debug")

    # reset_button = st.button(label="Reset", on_click=None, type="primary")
    table_button = st.button(label="Filter & Sort Data", type="secondary")
    progi_button = st.button(label="Show wdl graphs", type="secondary")
    configout_button = st.button(label="Show Configuration", type="secondary")

if table_button:
    config.set_config_dict(handle_configout_click())
    config.set_mode("FilterSort")
    config.set_loop(bool(loop_cb))
    config.set_debug(bool(debug_cb))
    config.set_country(selected_country.upper())
    config.set_league(selected_league_display)
    
    with debug_out.timed():
        with st.spinner("Please wait... Running the task"):
            adapted_df = data_adapter.adapt(league_path, extended_ml_model=False)
            with st.container(border=True):
                if loop_cb:
                    for side_team_name in unique_combined:
                        config.set_side_team(side_team_name)
                        df = stats_filter_sort.filter_and_sort_df(adapted_df)
                        st.write(df)
                else:
                    df = stats_filter_sort.filter_and_sort_df(adapted_df)
                    st.write(df)

if progi_button:
    config.set_config_dict(handle_configout_click())
    config.set_mode("Stat")
    config.set_loop(bool(loop_cb))
    config.set_debug(bool(debug_cb))
    config.set_country(selected_country.upper())
    config.set_league(selected_league_display)

    with debug_out.timed():
        with st.spinner("Please wait... Running the task"):
            adapted_df = data_adapter.adapt(league_path, extended_ml_model=False)
            if loop_cb:
                for side_team_name in unique_combined:
                    config.set_side_team(side_team_name)
                    modes_controller.select_mode(adapted_df)
            else:
                modes_controller.select_mode(adapted_df)

            config.set_loop(False)
            config.set_debug(False)

if configout_button:
    handle_configout_click(show=True)


if __name__ == "__main__":
    pass
