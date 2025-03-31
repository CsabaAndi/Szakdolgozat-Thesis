import dataman.mh_data_man as mh_data_man
import pandas as pd
import os
import debug_out
import streamlit as st
from pathlib import Path



def clean_preprocessed_jsons(raw_file):
    '''Generates cleaned out json files from the raw json files for mh'''
    out_path = raw_file.replace("preprocessed", "processed")
    directory_path = os.path.dirname(out_path)
    os.makedirs(directory_path, exist_ok=True)

    df = mh_data_man.match_history_preclean(raw_file)
    df.to_json(out_path)
    with st.container(border=True):
        st.success(f"Generated clean JSON files saved to {out_path}")
    
    new = pd.read_json(out_path)
    new['Date'] = pd.to_datetime(new['Date'], format=r'%d/%m/%y').dt.date
    debug_out.print_df(new)
    
    
    



if __name__ == "__main__":
    pass