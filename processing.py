from helper import *
from constants import *



def add_information(df):
    """Gathering information from the posts and putting them into a dictionary"""
    for feature in INPUT_FEATURES:
        func = INPUT_FEATURES[feature]
        calculated_attr = []
        for index, row in df.iterrows():
            calculated_attr.append(func(row))
        df[feature] = calculated_attr
    return df
