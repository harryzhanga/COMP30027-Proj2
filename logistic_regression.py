import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


def logistic_regression(train, test):
    posts = test["post"].values
    y_train = train["age"].values
    X_train = train.drop(columns = ["age", "post"]).values
    y_test = test["age"].values
    X_test = test.drop(columns = ["age", "post"]).values

    regr = linear_model.LogisticRegression()
    regr.fit(X_train, y_train)

    model_pred = regr.predict(X_test)
    mse = mean_squared_error(model_pred, y_test)
    print("Mean squared error: {:.2f}".format(mse))
    # for pred, actual, post in zip(model_pred, y_test, posts):
    #     if abs(pred-actual) > 10:
    #         print(pred, actual, post)
