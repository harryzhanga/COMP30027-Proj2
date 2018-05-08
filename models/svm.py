import pandas as pd
from sklearn.svm import SVC

def svm(target, explanatory, test_target, test_explanatory):
    regr = SVC()
    regr.fit(explanatory, target)
    model_pred = regr.predict(test_explanatory)
    for pred, actual in zip(model_pred, test_target):
        print(pred, actual)
