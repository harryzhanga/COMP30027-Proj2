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
    mse = mean_squared_error(model_pred, y_test)
    print("Mean squared error: {:.2f}".format(mse))

    #print("Regression model", regr.coef_, regr.intercept_)

    # for pred, actual in zip(model_pred, y_test):
    #     print(pred)
    return model_pred
