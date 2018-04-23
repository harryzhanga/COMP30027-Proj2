import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


def linear_regression(target, explanatory, test_target, test_explanatory):
    regr = linear_model.LinearRegression()
    regr.fit(explanatory, target)

    model_pred = regr.predict(test_explanatory)
    mse = mean_squared_error(model_pred, test_target)
    print("Mean squared error: {:.2f}".format(mse))
    print("Regression model", regr.coef_, regr.intercept_)
    for pred, actual in zip(model_pred, test_target):
        print(pred, actual)
