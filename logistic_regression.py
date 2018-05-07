import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


def logistic_regression(train, test):
    posts = test["post"].values
    target = train["age"].values
    explanatory = train.drop(columns = ["age", "post"]).values
    test_target = test["age"].values
    test_explanatory = test.drop(columns = ["age", "post"]).values

    regr = linear_model.LogisticRegression()
    regr.fit(explanatory, target)

    model_pred = regr.predict(test_explanatory)
    mse = mean_squared_error(model_pred, test_target)
    print("Mean squared error: {:.2f}".format(mse))
    #print("Regression model", regr.coef_, regr.intercept_)
    #
    # for pred, actual, post in zip(model_pred, test_target, posts):
    #     if abs(pred-post) > 10:
    #         print(pred, actual, post)
    #
