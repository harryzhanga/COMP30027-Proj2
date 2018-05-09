from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from constants import *
from processing import *

def model_decision_tree(train):
    y_train = train[AGE].values
    X_train = train.drop(columns = [AGE]).values
    # Entropy performs slightly better
    dt = DecisionTreeClassifier(criterion='entropy')
    dt.fit(X_train, y_train)
    return dt

def print_accuracy(y, predictions):
    """Prints accuracy statistics for class predictions made, given actual (y) classes"""
    assert(len(y)==len(predictions))
    correct = 0
    for i in range(len(y)):
        if y[i] == predictions[i]:
            correct += 1
    print("correct: {}/{}".format(correct, len(y)))
    print("accuracy: {:.2%}".format(correct/len(y)))

def evaluate_decision_tree(dt, test):
    y_test = test[AGE].values
    X_test = test.drop(columns = [AGE]).values
    dt_predictions = dt.predict(X_test)
    #print_accuracy(y_test, dt_predictions)

    l = []
    for pred, actual in zip(dt_predictions, y_test):
        l.append(get_age_from_bucket(pred))
    return l
