import numpy as np
import pandas as pd
import tensorflow as tf


import sys
import os

# Add the project root directory to sys.path
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(root_path)

from CONFIG import Config


config = Config()



def asd():
    path = r"../output/data/processed/match-history/compressed/all_countries.json"
    ''''''
    x = tf.constant([[1., 2., 3.],
                    [4., 5., 6.]])

    print(x)
    print(x.shape)
    print(x.dtype)
    
    

    config.print_config()

    

if __name__ == "main":
    asd()