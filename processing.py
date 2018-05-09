from helper import *
from constants import *
import pandas as pd
import nltk
import re

def get_age_from_bucket(bucket):
    if bucket == 0:
        return 15
    if bucket == 1:
        return 25
    if bucket == 2:
        return 35
    if bucket == 3:
        return 45
    return '?'

def get_bucket(age):
    """Accepts an age range string and returns its age bucket as an integer between 0 and 4 (inclusive)"""
    if age == "14-16" or age in range(14, 17):
        return 0
    if age == "24-26" or age in range(24, 27):
        return 1
    if age == "34-36" or age in range(34, 37):
        return 2
    if age == "44-46" or age in range(44, 47):
        return 3
    else:
        return 4

def make_top_10(df):
    new = pd.DataFrame()
    texts = df["text"]

    for word in set(WORD_COUNT_LIST):
        l = []
        for post in texts:
            splitted = clean(post).lower().split()
            l.append(splitted.count(word))
        new[word+"_count"] = l

    l = []
    for age in df[AGE]:
        bucket = get_bucket(age)
        l.append(bucket)
    new[AGE] = l
    return new





def clean(word):
    #return re.sub("""[^a-zA-Z\.\,\!\)\(\ \?\&]+""", '', word)
    return re.sub("""[^a-z\.\,\!\ \?]+""", '', word.lower())


def n_grams(df, n):
    """Returns a new df of ngrams"""
    d = {}
    for age, text in zip(df[AGE], df["text"]):
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
    for age, text in zip(df[AGE], df["text"]):
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
    for age, text in zip(df[AGE], df["text"]):
        new = {}
        new[AGE] = age
        for feature in TEXT_FEATURES:
            func = TEXT_FEATURES[feature]
            new[feature] = func(text)

        #tokenizing takes a while
        #splitted = [clean(word) for word in nltk.word_tokenize(text.lower())]
        splitted = clean(text).lower().split()
        for word in set(WORD_COUNT_LIST):
            new[word+"_count"] = splitted.count(word)
        d[i] = new
        i += 1
    return pd.DataFrame.from_dict(d, orient = "index")

def process_all(df):
    l = []
    for linear, knn, dt in zip(df["linear"], df["k_nn"], df["dt"]):
        if type(dt) == int:
            l.append((linear+knn+dt)/3)
        else:
            l.append((linear+knn)/2)
    return l
    
