import pandas as pd
import visual.graphs as graphs
import debug_out
import streamlit as st


def containered_dataframe(df, label):
    with st.container(border=True):
        st.markdown(f''':red[{label}]''')
        st.write(df)


## ----------------------------------------------------------- [ TABLES ] -------------------------------------------------------------------------------

def last_stats(dataframe):

    # TODO: Implement filter/sort by wdl
    # TODO: Implement filter/sort by last five

    df = dataframe.copy(deep=True)

    df["Wins"] = df["LastFive"].apply(lambda x: x.count("W"))
    df["Win_%"] = df["Wins"].apply(lambda x: ((x/5)*100))
    df["Draws"] = df["LastFive"].apply(lambda x: x.count("D"))
    df["Draw_%"] = df["Draws"].apply(lambda x: ((x/5)*100))
    df["Losses"] = df["LastFive"].apply(lambda x: x.count("L"))
    df["Loss_%"] = df["Losses"].apply(lambda x: ((x/5)*100))

    debug_out.print_df(df)
    
    containered_dataframe(df=df, label="LAST")

    return 0


def ou_stats(dataframe):

    # TODO: Implement count goal numbers 0-over 7
    # TODO: Implement stat goal number count 0 - 7+ divided by matches played
    # TODO: Implement over / under goals count (between)
    # TODO: Implement minden stat leosztva matches played vmi avg median vagy akármi

    df = dataframe.copy(deep=True)

    debug_out.print_df(df)
    
    containered_dataframe(df=df, label="OU")

    return 0


def player_stats(dataframe):

    df = dataframe.copy(deep=True)

    # TODO: Implement filter/sort by GOALS (between) | PENALTIES (between) | FIRSTGOALS (between) 
    # TODO: Implement TEAMNAME count teams  | team : count
    # TODO: Implement all penalties / team (one team more than once in top 15)
    # TODO: Implement all goals / team (one team more than once in top 15)
    # TODO: Implement all forst goals / team (one team more than once in top 15)

    debug_out.print_df(df)
    
    containered_dataframe(df=df, label="PLAYER")

    return 0

def wide_stats(dataframe):

    df = dataframe.copy(deep=True)


    debug_out.print_df(df)
    
    containered_dataframe(df=df, label="WIDE")

    return 0

## ---------------------------------------------------------------- [ TABLES ] --------------------------------------------------------------------------

#### ---------------------------------------------------------------- [STATS] ----------------------------------------------------------------------------






#### ----------------------------------------------------------------- [RANG ]-------------------------------------------------------------------







### -----------------------------------------------------------------[ RANG ]-------------------------------------------------------------------


