import streamlit as st
import sys
import os


# Add the path to the root folder to sys.path
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(root_path)

# Now you can import CONFIG
import debug_out
import file_loop.file_io as file_io
from CONFIG import Config


config = Config()

st.set_page_config(
    page_title="Match History",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

container = st.container(border=True)
col = st.columns((1.5, 4.5, 2), gap='medium')

# Function to handle the Configout button click
def handle_configout_click():
    # Capture all widget values with the new naming convention
    selected_values = {
        "Side-checkbox": bool(side_filter_cb),
        "Side-value": side_rb,
        "League-checkbox": bool(league_filter_cb),
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
        "Goal-sort-column": goal_col_s,
        "Goal-sort-order": bool(),  # Placeholder for goal_asc_rb.value
        "Date-checkbox": bool(date_filter_cb),
        "Date-start-end-format": r'%d/%m/%Y',
        "Date-sort": bool(date_sort_cb),
        "Date-filter-start": start_date_dp.strftime('%d/%m/%Y'),
        "Date-filter-end": end_date_dp.strftime('%d/%m/%Y'),
        "Date-sort-order": bool()  # Placeholder for date_asc_rb.value
    }

    # Display the values in the placeholder
    with col[1]:
        container.write("### Selected Values:")
        for key, value in selected_values.items():
            container.write(f"- {key}: {value}")
        
    return selected_values


with st.sidebar:

    # Side filter
    side_filter_cb = st.checkbox(label="Side filter")
    side_rb = st.radio(label="Side Filter Values", options=["Team_X", "Team_Y"], horizontal=True, key=1)

    # League filter
    league_filter_cb = st.checkbox(label="League filter")

    # WDL filter
    wdl_filter_cb = st.checkbox(label="WDL filter")
    wdl_rb = st.radio(label="WDL Filter Values", options=["win", "draw", "lose"], horizontal=True, key=2)

    # Goal filter
    goal_filter_cb = st.checkbox(label="Goal filter")
    bound_rb = st.radio(label="Goal Filter Values", options=["all", "X", "Y"], horizontal=True, key=3)

    # Number inputs for goals
    all_min_bi = st.number_input(label="all_min", min_value=0, max_value=100, value=0, step=1, key=100)
    all_max_bi = st.number_input(label="all_max", min_value=0, max_value=100, value=100, step=1, key=150)
    x_min_bi = st.number_input(label="x_min", min_value=0, max_value=100, value=0, step=1, key=200)
    x_max_bi = st.number_input(label="x_max", min_value=0, max_value=100, value=100, step=1, key=250)
    y_min_bi = st.number_input(label="y_min", min_value=0, max_value=100, value=0, step=1, key=300)
    y_max_bi = st.number_input(label="y_max", min_value=0, max_value=100, value=100, step=1, key=350)

    # Goal sort
    goal_sort_cb = st.checkbox(label="Goal Sort")
    goal_col_s = st.text_input(label="Goal col name", value="all_goals", key=500)
    goal_asc_rb = st.radio(label="Goal Sort asc/desc", options=["Ascending", "Descending"], horizontal=True, key=4)

    # Date filter
    date_filter_cb = st.checkbox(label="Date Filter")
    start_date_dp = st.date_input(label="Date-start", value="today", format='DD/MM/YYYY', key=10)
    end_date_dp = st.date_input(label="Date-end", value="today", format='DD/MM/YYYY', key=20)

    # Date sort
    date_sort_cb = st.checkbox(label="Date Sort")
    date_asc_rb = st.radio(label="Date Sort asc/desc", options=["Ascending", "Descending"], horizontal=True, key=5)

    # loop
    loop_cb = st.checkbox(label="(TMP) Loop")

    # debug (dev)
    debug_cb = st.checkbox(label="(dev) debug")

    # Buttons
    reset_button = st.button(label="Reset", on_click=None, type="primary")
    progi_button = st.button(label="Start", type="secondary")
    configout_button = st.button(label="Configout", type="secondary")
    


if progi_button:
    
    # Initialize config objects
    #GUI_mode_Config = CONFIG.ModeConfig("MatchHistory")
    #GUI_Match_History_Config = CONFIG.MatchHistoryConfig(config_dict=handle_configout_click())
    
    # TODO: na ez aszért bad mert init után lesz mindig értéke és ha van értlke akk rosszul hivpodik a match case mostan ibad !!!!!!!
    # ezé itt ""
    #GUI_table_type_Config = CONFIG.TableTypeConfig("")
    
    config.set_match_history_config(handle_configout_click())
    config.set_mode("MatchHistory")
    config.set_table_type("tabletype")
    config.set_loop(bool(loop_cb))
    config.set_debug(bool(debug_cb))
    
    with debug_out.timed():
        with st.spinner('Please wait... Running the task'):
            file_io.read_all_files_in_dir(st)
            config.set_loop(False)
            config.set_debug(False)
    

if configout_button:
    handle_configout_click()



if reset_button:
    with col[2]:
        container.write("Placeholder")
    
    

        
    
    
if __name__ == "__main__":
    pass
    