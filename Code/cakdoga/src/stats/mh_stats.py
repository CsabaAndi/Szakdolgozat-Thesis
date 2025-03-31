import pandas as pd

import visual.graphs as graphs
import dataman.mh_data_man as mh_data_man
import debug_out


import CONFIG


tmp_df = pd.DataFrame(columns=["team", "won", "draw", "lost"])
tmp_counter = 0


#### ---------------------------------------------------------- [ STATS ] -------------------------------------------------------------------------------

## -------------------------------------------------------- [ MATCH HISTORY ] ---------------------------------------------------------------------------

def mh_stats(mh_preclean_df):
    """[FILTEREZÉS]"""
    global tmp_df
    config = CONFIG.Config()
    Configuration = config.get_match_history_config()
    #Configuration = gui.GUI_Match_History_Config
    most_common_team = mh_data_man.mh_get_mcommon_team(mh_preclean_df)[0]
    

    # TODO: WIP | tesztnmek jo de szar refact !!
    mh_data_man.set_df_goal_cols(df=mh_preclean_df, column_name="Score", filter=False, min_goals=0, max_goals=100) # what ????

    # set wdl column data
    mh_preclean_df["wdl"] = mh_preclean_df.apply(lambda x: mh_data_man.set_df_wdl_col(x["Score"], x["Team_X"], most_common_team), axis=1)

    # side filter | home | away | all
    # col: Team_X --> home | col: Team_Y --> away  | filter: False --> All data
    # TODO: maradjon ez a side vagy legyen külön home/away/all ???
    side_filtered_df = mh_data_man.filter_df_by_col_value(mh_preclean_df, column_name=Configuration["Side-value"], filter=Configuration["Side-checkbox"], filter_value=most_common_team)
    
    # league filter
    # get league types then filter league col
    league_types = mh_data_man.mh_get_league_names(mh_preclean_df)
    # league_types[0] most played league
    league_filtered_df = mh_data_man.filter_df_by_col_value(side_filtered_df, column_name="League", filter=Configuration["League-checkbox"], filter_value=league_types[0])


    # TODO: ez most all df alapján nem veszi külön hogy home or away !!!
    goal_filtered_df = mh_data_man.filter_df_by_goals(league_filtered_df, filter=Configuration["Goal-checkbox"], filter_mode=Configuration["Goal-mode"], 
                                                      all_g_between_low=Configuration["Goal-between-all-low"], all_g_between_high=Configuration["Goal-between-all-high"], 
                                                      x_g_between_low=Configuration["Goal-between-x-low"], x_g_between_high=Configuration["Goal-between-x-high"], 
                                                      y_g_between_low=Configuration["Goal-between-y-low"], y_g_high=Configuration["Goal-between-y-high"], sort=Configuration["Goal-sort-checkbox"],
                                                      sort_col=Configuration["Goal-sort-column"], sort_asc=Configuration["Goal-sort-order"])

    # TODO: filter goal difference pl: 3-1 --> 2 vel nyert vagy mennyivel vesztett

    # wdl filter
    # win | draw | lose
    wdl_filtered_df = mh_data_man.filter_df_by_col_value(goal_filtered_df, column_name="wdl", filter=Configuration["Wdl-checkbox"], filter_value=Configuration["Wdl-value"])

    # date filter
    # start / end format | between start and end date | order
    date_sorted_filtered_df = mh_data_man.filter_sort_df_by_date(wdl_filtered_df, date_filter=Configuration["Date-checkbox"], date_column="Date", date_format=Configuration["Date-start-end-format"], 
                                                                start_date=Configuration["Date-filter-start"], end_date=Configuration["Date-filter-end"], date_sort= Configuration["Date-sort"],
                                                                ascending=Configuration["Date-sort-order"])   

    debug_out.print_df(date_sorted_filtered_df)

    tmp = df_wdl_counter(date_sorted_filtered_df, most_common_team)
    
    tmp_df = pd.concat([tmp, tmp_df])


    return 0


# TODO: WIP
def df_wdl_counter(df, team):
    """ Counts wdl 

    Keyword arguments:
    valami -- asd
    """
    config = CONFIG.Config()

    wdl_count = df["wdl"].value_counts()

    # ---------------------------------------------------------------- [TODO] ---------------------------------------------
    # tezstelésre jo muxik , de nagyon kell a refactor rá
    df_filtered_wdl_col = df["wdl"]
    df_wdl = pd.DataFrame(columns=["team", "won", "draw", "lost"])
    
   
    
    tmp_win_count = 0
    tmp_draw_count = 0
    tmp_lose_count = 0
    if "win" in wdl_count.index:
        tmp_win_count = df_filtered_wdl_col.value_counts()["win"]
    if "draw" in wdl_count.index:
        tmp_draw_count = df_filtered_wdl_col.value_counts()["draw"]
    if "lose" in wdl_count.index:
        tmp_lose_count = df_filtered_wdl_col.value_counts()["lose"]
        
    df_wdl.loc[0] = [team, str(tmp_win_count), str(tmp_draw_count), str(tmp_lose_count)]
    # ---------------------------------------------------------------- [TODO] ---------------------------------------------
    
    """
    # for TESTING
    for x in range(1,10,1):
        df_wdl.loc[x] = [f"szia mia ({str(x)})", str(x + 10), str(x + 20), str(x + 30)]
    """
    
    if config.get_debug() is True:
        # TODO: tmp false érték 0 ha wdl filter van és nincs benne ????
        print(f"---------------[{CONFIG.COLORS["WHITE"] + team + CONFIG.COLORS["RESET"]}]--------------------\n"
            f"won: {CONFIG.COLORS["GREEN"] + str(tmp_win_count) + CONFIG.COLORS["RESET"]}, draw: {CONFIG.COLORS["YELLOW"] + str(tmp_draw_count) + CONFIG.COLORS["RESET"]}, lost: {CONFIG.COLORS["RED"] + str(tmp_lose_count) + CONFIG.COLORS["RESET"]}\n"
            f"---------------------------------------")
                
    
    
    #graphs.wdl(df_wdl)

    return df_wdl


def tmpp():
    global tmp_df
    print(tmp_df.to_string())

def graph():
    """ graph """
    global tmp_df
    debug_out.print_df(tmp_df)
    graphs.wdl(tmp_df)

    
def empty_tmp_df():
    """ empties the global tmp_df dataframe """
    global tmp_df
    tmp_df = tmp_df.iloc[0:0]
    #print(tmp_df.to_string())


    
## -------------------------------------------------------- [ MATCH HISTORY ] ---------------------------------------------------------------------------




if __name__ == "__main__":
    pass