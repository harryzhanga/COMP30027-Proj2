from helper import *
from constants import *
import pandas as pd
import nltk
import re


def clean(word):

    return re.sub("""[^a-zA-Z\.\,\!\)\(\ \?\&]+""", '', word)
    #return re.sub("""[^a-zA-Z\.\,\!\ \?]+""", '', word.lower())


def n_grams(df, n):
    """Returns a new df of ngrams"""
    d = {}
    for age, text in zip(df["Age"], df["text"]):
        if age not in d:
            d[age] = {}
        ngrams = d[age]
        text = text.strip()
        text = clean(text)
        for i in range(len(text)-n+1):
            gram = text[i:i+n]
            ngrams[gram] = ngrams.get(gram, 0) + 1
    df = pd.DataFrame.from_dict(d, orient = "index")
    df.index.names = [AGE]
    return df.fillna(0)

def convert_n_grams(df, n):
    d = {}
    j = 0
    for age, text in zip(df["Age"], df["text"]):
        d[j] = {}
        ngrams = d[j]
        ngrams[AGE] = age
        text = text.strip()
        text = clean(text)
        for i in range(len(text)-n+1):
            gram = text[i:i+n]
            ngrams[gram] = ngrams.get(gram, 0) + 1
        j += 1
    df = pd.DataFrame.from_dict(d, orient = "index")
    return df.fillna(0)

def add_information(df):
    """Gathering information from the posts and putting them into a dictionary"""
    d = {}
    i = 0
    for age, text in zip(df["Age"], df["text"]):
        new = {}
        new[AGE] = age
        new["post"] = text

        for feature in TEXT_FEATURES:
            func = TEXT_FEATURES[feature]
            new[feature] = func(text)

        #tokenizing takes a while
        #splitted = [clean(word) for word in nltk.word_tokenize(text.lower())]
        splitted = clean(text).lower().split()
        for word in WORD_COUNT_LIST:
            new[word+"_count"] = splitted.count(word)
        d[i] = new
        i += 1
    return pd.DataFrame.from_dict(d, orient = "index")
