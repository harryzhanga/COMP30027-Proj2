import pandas as pd
from sklearn import neighbors
from sklearn.metrics import mean_squared_error, r2_score
from processing import *
from constants import *
import numpy as np

def evaluate_k_nn(knn, test):
    y_test = test[AGE].values
    X_test = test.drop(columns = [AGE]).values
    model_pred = knn.predict(X_test)
    mse = mean_squared_error(model_pred, y_test)
    print("Mean squared error: {:.2f}".format(mse))
    # for pred, actual in zip(model_pred, y_test):
    #     print(pred)
    return model_pred
    
def model_knn(train):
    y_train = train[AGE].values
    X_train = train.drop(columns = [AGE]).values
    knn = neighbors.KNeighborsRegressor(n_neighbors=2)
    knn.fit(X_train, y_train)
    return knn


def reconcile(df1, df2, default_value = 0):
    """Gives two dfs the same columns"""
    df1_cols = set(df1.columns.values)
    df2_cols = set(df2.columns.values)
    new = pd.DataFrame(default_value, index=np.arange(len(df2)), columns=list(df1_cols-df2_cols))
    df2 = pd.concat([df2, new], axis=1)
    new = pd.DataFrame(default_value, index=np.arange(len(df1)), columns=list(df2_cols-df1_cols))
    df1 = pd.concat([df1, new], axis=1)
    return df1, df2

def normalise(df):
    y = df[AGE]
    X = df.drop(columns = [AGE])
    X = X.div(df.sum(axis=1), axis=0)
    X[AGE] = y
    return X
