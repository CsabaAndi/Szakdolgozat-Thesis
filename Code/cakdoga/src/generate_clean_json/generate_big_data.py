import os
import pandas as pd
import streamlit as st

def generate_mh_big_data():
    # Base directory containing country folders
    base_dir = r"../output/data/processed/match-history"

    # Output directory for combined JSON files
    output_dir = r"../output/data/processed/match-history/compressed"
    os.makedirs(output_dir, exist_ok=True)

    # Initialize a list to store all combined data
    all_countries_data = pd.DataFrame()


    # Loop through each country folder
    for country_folder in os.listdir(base_dir):
        country_path = os.path.join(base_dir, country_folder).replace("\\", "/")
        print(country_path)
        # Skip if it's not a directory
        if not os.path.isdir(country_path):
            continue
        if country_path.split("/")[-1] == "compressed":
            continue
        
        # Initialize a list to store data for the current country
        country_data = pd.DataFrame()
        
        # Loop through all JSON files in the country folder
        for filename in os.listdir(country_path):
            if filename.endswith(".json"):
                file_path = os.path.join(country_path, filename)
                c_df = pd.read_json(file_path)

                country_data = pd.concat([country_data, c_df], ignore_index=True)
                
        # Save the combined data for the current country
        country_output_file = os.path.join(output_dir, f"{country_folder}.json").replace("\\", "/")
        country_data.to_json(country_output_file)
        print(f"Combined JSON for {country_folder} saved to {country_output_file}")
        
        # Append the country data to the all-countries list
        all_countries_data = pd.concat([all_countries_data, country_data], ignore_index=True)

    # Save the combined data for all countries
    all_countries_output_file = os.path.join(output_dir, "all_countries.json").replace("\\", "/")
    all_countries_data.to_json(all_countries_output_file)
    print(f"Combined JSON for all countries saved to {all_countries_output_file}")
    with st.container(border=True):
        st.success(f"Combined JSON for all countries saved to {all_countries_output_file}")
        #st.json(all_countries_data.to_json(orient="records"))
    all_countries_data = pd.DataFrame()
 
    

def generate_tables_big_data(config):
    
    # Base directory containing country folders
    base_dir = r"../output/data/preprocessed/tables"

    # Output directory for combined JSON files
    output_dir = r"../output/data/processed/tables/compressed"
    os.makedirs(output_dir, exist_ok=True)

    # Initialize a list to store all combined data
    all_tables_data = pd.DataFrame()

    table_type = ""

    match config.get_table_type():
        case "Last":
            table_type = "LastFive"
        case "Ou":
            table_type = "OverUnder"
        case "Player":
            table_type = "Player"
        case "Wide":
            table_type = "Wide"
          


    for root, dirs, files in os.walk(base_dir, topdown=False):
        for file in files:
            if file.endswith(f"{table_type}.json"):
                print(root)
                print(file)
                file_path = os.path.join(root, file)
                print(file_path)
                t_df = pd.read_json(file_path)
                all_tables_data = pd.concat([all_tables_data, t_df], ignore_index=True)

    # Save the combined data for all countries
    all_countries_output_file = os.path.join(output_dir, f"all_tables_{table_type}.json").replace("\\", "/")
    all_tables_data.to_json(all_countries_output_file)
    print(f"Combined JSON for all {table_type} tables saved to {all_countries_output_file}")
    with st.container(border=True):
        st.success(f"Combined JSON for all '{table_type}' tables saved to {all_countries_output_file}")
        #st.json(all_tables_data.to_json(orient="records"))
    all_tables_data = pd.DataFrame()
    


if __name__ == "__main__":
    pass