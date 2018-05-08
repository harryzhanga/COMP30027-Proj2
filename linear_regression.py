import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from constants import *
from sklearn.decomposition import PCA



def linear_regression(train, test, use_PCA = False):
    posts = test["post"].values
    y_train = train[AGE].values
    X_train = train.drop(columns = [AGE, "post"]).values

    y_test = test[AGE].values
    X_test = test.drop(columns = [AGE, "post"]).values

    if use_PCA:
        sklearn_pca = PCA(n_components = 4)
        X_test = sklearn_pca.fit_transform(X_test)
        X_train = sklearn_pca.fit_transform(X_train)

    regr = linear_model.LinearRegression()
    regr.fit(X_train, y_train)
    model_pred = regr.predict(X_test)
    mse = mean_squared_error(model_pred, y_test)
    print("Mean squared error: {:.2f}".format(mse))
    #print("Regression model", regr.coef_, regr.intercept_)

    # for pred, actual, post in zip(model_pred, y_test, posts):
    #     if abs(pred-actual) > 10:
    #         print(pred, actual, post)
