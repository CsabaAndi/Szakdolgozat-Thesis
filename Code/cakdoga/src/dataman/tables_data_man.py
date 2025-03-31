import pandas as pd
from datetime import datetime


def table_last_preclean(file):

    # TODO: Implement preclean last five

    df_last = pd.read_json(file)

    df_last_copy = df_last.copy(deep=True)


    return df_last_copy


def table_ou_preclean(file):

    df_ou = pd.read_json(file)

    df_ou_copy = df_ou.copy(deep=True)


    return df_ou_copy



def table_player_preclean(file):

    df_player = pd.read_json(file)
    
    df_player_copy = df_player.copy(deep=True)


    return df_player_copy

def table_wide_preclean(file):

    df_wide = pd.read_json(file)

    df_wide_copy = df_wide.copy(deep=True)

    return df_wide_copy