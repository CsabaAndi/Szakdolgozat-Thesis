import pandas as pd


def read_input(test_file_path):
    data = pd.read_csv(test_file_path, sep=r'\t', header=0, index_col=None, engine='python') # index_col=0 | wide + ou
    df = pd.DataFrame(data)
    return df
   
    
if __name__ == "__main__":
    pass
