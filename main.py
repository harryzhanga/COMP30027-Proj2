import numpy as np
import pandas as pd
from constants import *
from processing import *
from evaluation import *
from linear_regression import *
from logistic_regression import *
from svm import *
from k_nn import *
from sklearn.model_selection import train_test_split


def parse_data(filename):
    """Reads the file and then extracts the ages and post columns from the dataset"""
    df = pd.read_csv(filename, names = ["User ID", "Gender", "Age", "Occupation", "Star Sign", "date", "text"])
    return df

def get_features(df):
    #check processing.py, this function just converts the df to new attributes that we think are interesting
    data = add_information(df)
    return data


def run_linear():
    print("RUNNING LINEAR")
    raw = parse_data(WINDOWS_SAMPLE_FILENAME)
    data = get_features(raw)
    #print(data.corr())
    data.to_csv("test.csv")
    train, test = train_test_split(data, test_size=0.1)
    linear_regression(train, test, use_PCA = True)

def run_k_nn():
    print("RUNING KNN")
    model_knn("data/3grams_sample.csv")
    evaluate_k_nn("data/3grams_sample.csv", WINDOWS_SAMPLE_FILENAME)

#run_linear()
#run_k_nn()

#logistic_regression(train, test)
