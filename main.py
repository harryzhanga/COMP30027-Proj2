import numpy as np
import pandas as pd
from constants import *
from processing import *
from evaluation import *
from models.linear_regression import *
from models.logistic_regression import *
from models.svm import *
from sklearn.model_selection import train_test_split


def parse_data(filename):
    """Reads the file and then extracts the ages and post columns from the dataset"""
    df = pd.read_csv(filename, names = ["User ID", "Gender", "Age", "Occupation", "Star Sign", "date", "text"])
    return df

def get_features(df):
    #check processing.py, this function just converts the df to new attributes that we think are interesting
    data = add_information(df)
    return data

def get_n_grams(df):
    return n_grams(df, 2)


raw = parse_data(WINDOWS_SAMPLE_FILENAME)
data = get_features(raw)
data.to_csv("data/features_sample.csv")
data2 = get_n_grams(raw)
data2.to_csv("data/ngrams_sample.csv")
#having a look at the correlation
#print(data.corr())
#data = pd.read_csv("data/test.csv")

#separate into training and test data
#train, test = train_test_split(data, test_size=0.1)

#models
#linear_regression(train, test)
#logistic_regression(train, test)
#svm(target_classes, explanatory, test_target_classes, test_explanatory)
