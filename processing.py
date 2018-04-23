from helper import *
from constants import *
import pandas as pd


def add_information(df):
    """Gathering information from the posts and putting them into a dictionary"""
    new = pd.DataFrame()
    new["age"] = df["Age"]
    new["post"] = df["text"]
    for feature in TEXT_FEATURES:
        func = TEXT_FEATURES[feature]
        calculated_attr = []
        for text in df["text"]:
            calculated_attr.append(func(text))
        new[feature] = calculated_attr
    return new
