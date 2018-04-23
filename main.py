import numpy as np
import pandas as pd
from constants import *
from processing import *
from evaluation import *

def parse_data(filename):
    """Reads the file and then extracts the ages and post columns from the dataset"""
    df = pd.read_csv(filename, names = ["User ID", "Gender", "Age", "Occupation", "Star Sign", "date", "text"])
    return df

#get the age and posts in two lists
df = parse_data(WINDOWS_SAMPLE_FILENAME)

#check processing.py
add_information(df)

df.to_csv("data/processed_sample.csv", index = False)
print("DONE!")
