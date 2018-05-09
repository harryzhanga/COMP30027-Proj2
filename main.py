import numpy as np
import pandas as pd
from constants import *
from processing import *
from evaluation import *
from linear_regression import *
from logistic_regression import *
from k_nn import *
from sklearn.model_selection import train_test_split
from decision_tree import *

def parse_data(filename):
    """Reads the file and then extracts the ages and post columns from the dataset"""
    df = pd.read_csv(filename, names = ["User ID", "Gender", AGE, "Occupation", "Star Sign", "date", "text"])
    return df


def run_linear(train, test):
    print("RUNNING LINEAR")
    #convert it to another dataframe with ages
    train = add_information(train)
    train.to_csv("test.csv")
    #print(data.corr())
    model = linear_regression(train)

    test = add_information(test)
    return evaluate_linear_regression(model, test)

def recover(df):
    df.to_csv("data/tmp.csv")
    return pd.read_csv("data/tmp.csv")

def run_k_nn(train, test):
    print("RUNING KNN")
    train = n_grams(train, N)
    test = convert_n_grams(test, N)
    train = recover(train)
    test = recover(test)

    #sum of row = 1
    test = normalise(test)
    train = normalise(train)

    #empty columns created
    train, test = reconcile(train, test)
    model = model_knn(train)
    return evaluate_k_nn(model, test)

def run_decision_tree(train, test):
    print("RUNNING DECISION TREE")
    train = make_top_10(train)
    test = make_top_10(test)
    model = model_decision_tree(train)
    return evaluate_decision_tree(model, test)

def run_all():
    data = parse_data(WINDOWS_SAMPLE_FILENAME)
    data = data[[AGE, "text"]].head(50)
    train, test = train_test_split(data, test_size=0.1)

    new = pd.DataFrame()
    linear_results = run_linear(train, test)
    k_nn_results = run_k_nn(train, test)
    dt_results = run_decision_tree(train, test)
    new["linear"] = linear_results
    new["k_nn"] = k_nn_results
    new["dt"] = dt_results
    all = process_all(new)
    new["overall"] = all
    new.to_csv(SAVE_LOCATION)

run_all()
