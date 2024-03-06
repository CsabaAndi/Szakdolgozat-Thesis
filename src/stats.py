import numpy as np
import file_io


def some_stat(dataframe=file_io.read_input(r'../test-data/0-wide-3000.csv')):
    np_array = dataframe['W-T'].to_numpy().flatten()
    print(np_array)
    array_mean = np.mean(np_array)
    return array_mean
    


if __name__ == "__main__":
    pass