import pandas as pd
import os 
import glob 
import stats
  
  
def read_all_files_in_dir(): # TODO file path
    table_type = "wide"
    path = r"../test-data/"
    csv_files = glob.glob(os.path.join(path, "*" + table_type + ".csv")) 

    for f in csv_files: 
        file_name = os.path.basename(f)
        name_without_extension = os.path.splitext(file_name)
        split_fn = name_without_extension[0].split('_')
        
        df = pd.read_csv(f, header=0, index_col=None, engine='python') 
        stats.some_stat(df)

        print(f"Country: {split_fn[0]} {'\n'}League: {split_fn[1]} {'\n'}Year: {split_fn[2]} {'\n'}Table_type: {split_fn[3]}")
        print(df.to_string())
        
    
    
if __name__ == "__main__":
    pass
