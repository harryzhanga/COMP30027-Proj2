from helper import *
from constants import *
import pandas as pd
import nltk

def clean(word):
    return word.replace(".", "").replace(",", "").replace("!", "").strip()

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

        #tokenizing takes a while
        splitted = [clean(word) for word in nltk.word_tokenize(text.lower())]
        for word in WORD_COUNT_LIST:
            new[word+"_count"] = splitted.count(word)
        d[i] = new
        i += 1
    return pd.DataFrame.from_dict(d, orient = "index")
