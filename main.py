import numpy as np
import pandas as pd
from constants import *
from processing import *
from evaluation import *
from linear_regression import *
from svm import *
from sklearn.model_selection import train_test_split


def parse_data(filename):
    """Reads the file and then extracts the ages and post columns from the dataset"""
    df = pd.read_csv(filename, names = ["User ID", "Gender", "Age", "Occupation", "Star Sign", "date", "text"])
    train, test = train_test_split(df, test_size=0.1)
    return train, test

#get the age and posts in two lists
train, test = parse_data(WINDOWS_SAMPLE_FILENAME)

#check processing.py
train = add_information(train)
test = add_information(test)


#having a look at the correlation
print(train.corr())

#separate the target and the explanatory variables for the linear model
#also converts to numpy arrays
target = train["age"].values
explanatory = train.drop(columns = ["age"]).values

test_target = test["age"].values
test_explanatory = test.drop(columns = ["age"]).values

linear_regression(target, explanatory, test_target, test_explanatory)
#svm(target_classes, explanatory, test_target_classes, test_explanatory)

#train.to_csv("data/processed_sample.csv", index = False)
