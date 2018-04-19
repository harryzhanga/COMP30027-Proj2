import numpy as np
import pandas as pd
from constants import *
from processing import *

def parse_data(filename):
    """Reads the file and then extracts the ages and post columns from the dataset"""
    df = pd.read_csv(filename, names = ["User ID", "Gender", "Age", "Occupation", "Star Sign", "Date", "Text"])
    age, posts = df["Age"], df["Text"]
    return age, posts

features = {
    SENTENCE_LENGTH : True,
    WORD_LENGTH : True
}

age, posts = parse_data(WINDOWS_SAMPLE_FILENAME)
info = get_information(age, posts, features)
info = process_features(info, features)
print(info)
