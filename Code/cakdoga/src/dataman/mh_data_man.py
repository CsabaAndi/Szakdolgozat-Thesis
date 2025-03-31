import pandas as pd
from datetime import datetime

import re



# DÁTUMOKRA FIGYELNI KELL mert táblázatok van ami nem a legfrisserbb pl : török super lig --> 23/24 a táblázat de már megsy a 24/25 season és historyban az már benne van !!!
# TODO: filter / sort minden egybe ???

#előfeldolgozés historyn a hasznos adathoz
def match_history_preclean(file):

    # convert false azért kell mert vmiért automatic convertálja a dateket szarul
    df_mh = pd.read_json(file, convert_dates=False) 

    # copy
    df_mh_copy = df_mh.copy(deep=True) 

    ### df_mh_copy.replace("NaN", "asd")

    # kivenni ami nem rendes score eredmény
    df_clean = df_mh_copy.loc[(~df_mh_copy["Score"].isin(["-", "CANC", "SUSP"])) & (~df_mh_copy["Score"].str.match("\d\d:\d\d", na=False))] # valamiért van nan??

    # date convert on copied df throws warning
    pd.options.mode.chained_assignment = None  # default='warn'
    # date convert hogy lehessen sortolni
    df_clean['Date'] = pd.to_datetime(df_clean['Date'], format=r'%d/%m/%y').dt.date

    return df_clean


def mh_get_mcommon_team(mh_df_all: pd.DataFrame) -> list[str]:
    """ Counts the teams in the whole df and returns a list of the most common team names.

    Keyword arguments:
        mh_df_all: Base Match history DataFrame

    Returns:
        most common team names list ([0] being the most common)
    """
    # most common team name
    team_name_counts = mh_df_all.stack().value_counts()
    most_common_team = team_name_counts[team_name_counts.eq(team_name_counts.max())].index.tolist()
    
    return most_common_team


def mh_get_league_names(mh_df_all: pd.DataFrame) -> list[str]:
    """ Returns a list of league names in descending order based on counts from the DataFrame.
    
    Keyword arguments:
        mh_df_all: Base Match history DataFrame

     Returns:
        list with league names ([0] being the most common)
    """    
    
    league_names_desc_list = mh_df_all["League"].value_counts().sort_values(ascending=False).index.to_list()
    
    return league_names_desc_list

# TODO: van hogy a táblázat üres sorok vagy data_man alapján kerül bele | pl: portugal estrela  és akkor a score nan és kiakad !!!!!!!!!!!!
def get_goals_helper(df_score_col: pd.DataFrame):
    # ha van benne betü
    if re.match(r".*[a-zA-Z].*", str(df_score_col)):
        # számokat listába regex  
        score = re.findall(r"\d+", str(df_score_col))
        s1 =  score[0]
        s2 = score[1]
    else:
        score = re.findall(r"\d+", str(df_score_col))
        s1 =  score[0]
        s2 = score[1]

    return [s1, s2]


# TODO: implement | tezstelésre jó de refactor mert szar az egész
def set_df_goal_cols(df: pd.DataFrame, column_name: str = "Score", filter: bool = False, min_goals: int = 0, max_goals: int = 100):

    def all(df_col):
        s1,s2 = get_goals_helper(df_col)

        return int(s1)+int(s2)
    
    def g_x(df_col):
        s1,s2 = get_goals_helper(df_col)

        return s1
    
    def g_y(df_col):
        s1,s2 = get_goals_helper(df_col)

        return s2

    
    
    df["Goal_X"] = df[column_name].apply(lambda x: g_x(x))
    df["Goal_Y"] = df[column_name].apply(lambda x: g_y(x))
    df["all_goals"] = df[column_name].apply(lambda x: all(x))

    # converting goal_X and Y from string to int
    df[["Goal_X", "Goal_Y"]] = df[["Goal_X", "Goal_Y"]].apply(pd.to_numeric, axis=1)

    return df


# TODO: refactor
def set_df_wdl_col(df_score_col: pd.DataFrame, df_team_x_col: pd.DataFrame, mcommon_team: str):
    """ Helper function to set Dataframe "wdl" column based on "Scores" column and "Team" column (home or away team)

    Keyword arguments:
        df_score_col: Dataframe "Score" column 
        df_team_x_col: Dataframe "Team_X" column
        mcommon_team: Most common team name (str)
        
    Returns:
        win / draw / lose based on score.
    """
    s1, s2 = get_goals_helper(df_score_col)

    # "home"
    x = s1
    y = s2
    
    if df_team_x_col != mcommon_team:
        # "away"
        x = s2
        y = s1 
    
    if (x > y):
        return "win"
    elif x == y:
        return "draw"
    else:
        return "lose"


# TODO: legyen -e inplace vagy copy df vagy vmi
def filter_sort_df_by_date(df: pd.DataFrame, date_filter: bool, date_column: str = "Date", date_format: str = r'%d/%m/%Y', start_date: str = "01/01/1010", end_date: str = "01/01/2100", date_sort: bool = False, ascending: bool = False) -> pd.DataFrame:
    """ Filters and sorts df between dates.

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

    date_filtered_df = df

    
    if date_filter == True:
        date_filtered_df = df.loc[df[date_column].between(datetime.strptime(start_date, date_format).date(), datetime.strptime(end_date, date_format).date())]


    if date_sort == True:
        date_sorted_df = date_filtered_df.sort_values(by=[date_column], ascending=ascending)
    else:
        date_sorted_df = date_filtered_df

        
    return date_sorted_df




def filter_df_by_col_value(df: pd.DataFrame, column_name: str = "League", filter: bool = False, filter_value: str = "win"):
    """ Filters df Column based on value

    Keyword arguments:
        df: DataFrame to filter
        column_name: Column name (str)
        filter: boolean to use the filter
        filter_value: filter value (str)

    Returns:
        filtered DataFrame
    """

    col_filtered_df = df

    if filter == True:
        col_filtered_df = df.loc[df[column_name] == filter_value]

    return col_filtered_df


# TODO: ez most all df alapján nem veszi külön hogy home or away !!!
def filter_df_by_goals(df: pd.DataFrame, filter: bool = False, filter_mode: str = "all", all_g_between_low: int = 0,  
                       all_g_between_high: int = 100, x_g_between_low: int = 0,  x_g_between_high: int = 100, 
                       y_g_between_low: int = 0,  y_g_high: int = 100, sort_col: str = "all_goals", sort: bool = False, sort_asc: bool = True):

    goal_filtered_df = df

    if filter == True:
        if filter_mode == "all":
           goal_filtered_df = df.loc[df["all_goals"].between(all_g_between_low, all_g_between_high)]
        elif filter_mode == "X" :
           goal_filtered_df = df.loc[df["Goal_X"].between(x_g_between_low, x_g_between_high)]
        elif filter_mode == "Y" :
            goal_filtered_df = df.loc[df["Goal_Y"].between(y_g_between_low, y_g_high)]

    if sort == True:
        # sort 
        #goal_sorted_df = goal_filtered_df.loc[goal_filtered_df[sort_col]].sort_values(ascending=sort_asc)
        goal_sorted_df = goal_filtered_df.sort_values(by=[sort_col], ascending=sort_asc)
    else:
        goal_sorted_df = goal_filtered_df

    return goal_sorted_df


if __name__ == "__main__":
    pass