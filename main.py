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
    model = linear_regression(train)

    test = add_information(test)
    return evaluate_linear_regression(model, test)

def recover(df):
    df.to_csv("data/tmp.csv")
    data = pd.read_csv('data/tmp.csv', error_bad_lines=False)
    return data

def run_k_nn(train, test, neighbours, n):
    print("RUNING KNN")
    train = n_grams(train, n)

    test = convert_n_grams(test, n)
    train = recover(train)
    test = recover(test)
    #sum of row = 1
    test = normalise(test)
    train = normalise(train)

    #empty columns created
    train, test = reconcile(train, test)

    train = train.reindex_axis(train.mean().sort_values().index, axis=1)
    test = test.reindex_axis(test.mean().sort_values().index, axis=1)

    model = model_knn(train, neighbours)
    return evaluate_k_nn(model, test)


def run_decision_tree(train, test):
    print("RUNNING DECISION TREE")
    train = make_top_10(train)
    test = make_top_10(test)
    model = model_decision_tree(train)
    return evaluate_decision_tree(model, test)

def run_all():
    train = parse_data(WINDOWS_FILENAME)
    train = train[[AGE, "text"]]
    test = parse_data(DEV_FILENAME)

    ID = list(test["User ID"])
    age = list(test[AGE])
    test = test[["text"]]
    test[AGE] = age

    new = pd.DataFrame()
    linear_results = run_linear(train.sample(5000), test)
    k_nn_results = run_k_nn(train.sample(500), test, 2, N)
    dt_results = run_decision_tree(train.sample(1000), test)
    new["linear"] = linear_results
    new["k_nn"] = k_nn_results
    new["dt"] = dt_results
    all = process_all(new)
    new["age"] = age
    new["overall"] = all
    new["ID"] = ID
    new.to_csv("data/dev_calculated.csv")

def bucket(x):
    if x < 20:
        return "14-16"
    if x > 40:
        return "44-46"
    if x > 30:
        return "34-36"
    return "24-26"
#run_all()
dev = pd.read_csv("data/all_results.csv")
from sklearn.metrics import mean_squared_error, r2_score
dev = dev.groupby('ID').mean()
ID = dev.index.values
overall = [bucket(x) for x in dev["overall"]]

new = pd.DataFrame()
new["ID"] =  ID
new["overall"] = overall
new.to_csv("data/final.csv")
