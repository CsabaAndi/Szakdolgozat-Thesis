import os
import pandas as pd
import itertools

import file_loop.call_stats as call_stats
import stats.mh_stats as mh_stats
import learning as learning
#import visual.gui as gui
#import stream.pages.page_two as gui

from CONFIG import Config


config = Config()



# TODO tmp mi a tök ez 
tmp_df = pd.DataFrame(columns=["team", "won", "draw", "lost"])
tmp_counter = 0


def json_to_csv(r, file):
    file_name_csv = os.path.splitext(file)[0]+'.csv'
    write_path = os.path.join(r, file_name_csv)
    df = pd.read_json(os.path.join(r, file)) 
    df.to_csv(write_path, encoding='utf-16', index=False, header=True)


# file_io.py
def read_all_files_in_dir(page): # TODO file path 
    global tmp_counter
    global tmp_df
    global table_type
    global path

    #Tablemodeconfig = gui.GUI_table_type_Config
    #ModeConfig = GUI_mode_Config
    Tablemodeconfig = config.get_table_type()
    ModeConfig = config.get_mode()

    loop = config.get_loop()

    mh = False

    match ModeConfig:
        case "Data":
            path = r"../output/data/preprocessed/match-history"
            table_type = ""
        case "MatchHistory":
            #path = r"../output/data/match-history"
            path = r"../output/data/preprocessed/match-history"
            table_type = ""
            mh = True
        case "Tables":
            path = r"../output/data/preprocessed/tables"
            match Tablemodeconfig: # LastFive | OverUnder | Player | Wide 
                case "Last":
                    table_type = "LastFive"
                case "Ou":
                    table_type = "OverUnder"
                case "Player":
                    table_type = "Player"
                case "Wide":
                    table_type = "Wide"
                    
    # TODO !!! valma iszar a table loopoknál
    # r=root, d=directories, f = files
    for r, d, f in itertools.islice(os.walk(path, topdown=True), 1, 50, 1):
        # folderenként!
        country = r.split("/")[-1]
        # windows céges env ez muxik (?)
        #config.set_country(country.split("\\")[1].upper())
        
        #linux ez (?)
        config.set_country(country.upper())
        for file in f:
            # teamenként
            # file: sheffield-united-fc.json
            if file.endswith(f"{table_type}.json"):
                file_path_name = os.path.join(r, file)
                call_stats.call_modes(file_path_name)
        #print(mh)
        if mh:
            #learning.ml.mltmp.asd()
            mh_stats.graph()
            mh_stats.empty_tmp_df()
            if loop is False:
                break
    return 0
    # Legvége!
    


if __name__ == "__main__":
    pass
