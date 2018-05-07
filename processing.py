from helper import *
from constants import *
import pandas as pd



def add_information(df):
    """Gathering information from the posts and putting them into a dictionary"""
    d = {}
    i = 0
    for age, text in zip(df["Age"], df["text"]):
        new = {}
        new["age"] = age
        new["post"] = text
        for feature in TEXT_FEATURES:
            func = TEXT_FEATURES[feature]
            new[feature] = func(text)
        splitted = text.upper().split()
        for feature in SPLIT_FEATURES:
            func = SPLIT_FEATURES[feature]
            new[feature] = func(splitted)
        d[i] = new
        i += 1
    return pd.DataFrame.from_dict(d, orient = "index")
