import numpy as np
import pandas as pd
from constants import *
from processing import *
from evaluation import *
from linear_regression import *
from logistic_regression import *
from svm import *
from sklearn.model_selection import train_test_split


def parse_data(filename):
    """Reads the file and then extracts the ages and post columns from the dataset"""
    df = pd.read_csv(filename, names = ["User ID", "Gender", "Age", "Occupation", "Star Sign", "date", "text"])
    return df

#get the age and posts in two lists
data = parse_data(WINDOWS_SAMPLE_FILENAME)

#check processing.py
data = add_information(data)
data.to_csv("data/test.csv", index = False)

#having a look at the correlation
#print(data.corr())

data = pd.read_csv("data/test.csv")
train, test = train_test_split(data, test_size=0.1)

#models
#linear_regression(train, test)
#logistic_regression(train, test)
#svm(target_classes, explanatory, test_target_classes, test_explanatory)
