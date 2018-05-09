import pandas as pd
from sklearn import neighbors
from sklearn.metrics import mean_squared_error, r2_score
from processing import *
from constants import *
import numpy as np

def evaluate_k_nn(knn, test):
    test = test.fillna(0)
    y_test = test[AGE].values
    X_test = test.drop(columns = [AGE]).values

    model_pred = knn.predict(X_test)
    # mse = mean_squared_error(model_pred, y_test)
    # print("Mean squared error: {:.2f}".format(mse))
    # d = {}
    # for pred, actual in zip(model_pred, y_test):
    #     d[pred] = d.get(pred, 0) +1
    # print(d)
    return model_pred

def model_knn(train, neighbours):
    train = train.fillna(0)
    y_train = train[AGE].values
    X_train = train.drop(columns = [AGE]).values
    knn = neighbors.KNeighborsRegressor(n_neighbors=neighbours)
    knn.fit(X_train, y_train)
    return knn


def reconcile(df1, df2, default_value = 0):
    """Gives two dfs the same columns"""
    df1_cols = set(df1.columns.values)
    df2_cols = set(df2.columns.values)
    l = [x for x in list(df1_cols-df2_cols) if len(x) >= 1]
    new = pd.DataFrame(default_value, index=np.arange(len(df2)), columns=l)
    df2 = pd.concat([df2, new], axis=1)
    l = [x for x in list(df2_cols-df1_cols) if len(x) >= 1]
    new = pd.DataFrame(default_value, index=np.arange(len(df1)), columns=l)
    df1 = pd.concat([df1, new], axis=1)
    return df1, df2

def normalise(df):
    y = df[AGE]
    X = df.drop(columns = [AGE])
    X = X.loc[:, ~X.columns.str.contains('^Unnamed')]
    X = X.div(X.sum(axis=1), axis=0)
    X[AGE] = y
    return X
