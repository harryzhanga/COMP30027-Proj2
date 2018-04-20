import numpy as np
import pandas as pd
from constants import *
from processing import *
from evaluation import *

def parse_data(filename):
    """Reads the file and then extracts the ages and post columns from the dataset"""
    df = pd.read_csv(filename, names = ["User ID", "Gender", "Age", "Occupation", "Star Sign", "Date", "Text"])
    age, posts = df["Age"], df["Text"]
    return age, posts

age, posts = parse_data(WINDOWS_SAMPLE_FILENAME)
info = get_information(age, posts)
processed_info = process_features(info)
print_nicely(processed_info)
