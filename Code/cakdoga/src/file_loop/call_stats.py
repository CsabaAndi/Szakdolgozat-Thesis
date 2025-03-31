import os
import pandas as pd

import dataman.mh_data_man as mh_data_man
import generate_clean_json.preclean
import stats.mh_stats as mh_stats
import stats.tables_stats as tables_stats
import dataman.tables_data_man as tables_data_man
import generate_clean_json

from CONFIG import Config


config = Config()


def call_modes(filepath):
    
    ModeConfig = config.get_mode()
    match ModeConfig:
        case "Data":
            call_data_clean_to_file(filepath)
        case "MatchHistory":
            call_mh(filepath)
        case "Tables":
            call_table(filepath)



def call_mh(filepath):
    if config.get_debug is True:
        print(f"Filepath: {filepath}")

    mh_stats.mh_stats(mh_data_man.match_history_preclean(filepath))


def call_table(filepath):
    Tablemodeconfig = config.get_table_type()
    if config.get_debug is True:
        print(f"Filepath: {filepath}")
    
    match Tablemodeconfig:
        case "Last":
            tables_stats.last_stats(tables_data_man.table_last_preclean(filepath))
        case "Ou":
            tables_stats.ou_stats(tables_data_man.table_ou_preclean(filepath))
        case "Player":
            tables_stats.player_stats(tables_data_man.table_player_preclean(filepath))
        case "Wide":
            tables_stats.wide_stats(tables_data_man.table_wide_preclean(filepath))  
    

    
def call_data_clean_to_file(filepath):
    ModeConfig = config.get_mode()
    if config.get_debug is True:
        print(f"Filepath: {filepath}")
    
    generate_clean_json.preclean.clean_preprocessed_jsons(filepath)


    
if __name__ == "__main__":
    pass
