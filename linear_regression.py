import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from constants import *
from sklearn.decomposition import PCA


def linear_regression(train):
    y_train = train[AGE].values
    X_train = train.drop(columns = [AGE]).values
    regr = linear_model.LinearRegression()
    regr.fit(X_train, y_train)
    return regr

def evaluate_linear_regression(regr, test):
    y_test = test[AGE].values
    X_test = test.drop(columns = [AGE]).values
    model_pred = regr.predict(X_test)
    # mse = mean_squared_error(model_pred, y_test)
    # print("Mean squared error: {:.2f}".format(mse))
    # print("Regression model")
    # for coef in regr.coef_:
    #     print("{0:.2f}".format(coef))
    # print("intercept", regr.intercept_)
    #
    # d = {}
    # for pred, actual in zip(model_pred, y_test):
    #     if actual not in d:
    #         d[actual] = {}
    #         age = d[actual]
    #         age["larger_count"] = 0
    #         age["smaller_count"] = 0
    #         age["larger_sum"] = 0
    #         age["smaller_sum"] = 0
    #     age = d[actual]
    #     if pred > actual:
    #         age["larger_count"] += 1
    #         age["larger_sum"] += (pred-actual)
    #     else:
    #         age["smaller_count"] += 1
    #         age["smaller_sum"] += (actual-pred)
    # df = pd.DataFrame.from_dict(d, orient = "index")
    # df.to_csv("data/linear_regression.csv")
    return model_pred
