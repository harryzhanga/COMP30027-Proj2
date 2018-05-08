import pandas as pd
from sklearn import neighbors
from sklearn.metrics import mean_squared_error, r2_score
from processing import *
from constants import *
import numpy as np

def k_nn(train, test):
    y_train = train[AGE].values
    X_train = train.drop(columns = [AGE]).values
    y_test = test[AGE].values
    X_test = test.drop(columns = [AGE]).values
    knn = neighbors.KNeighborsRegressor(n_neighbors=2)
    knn.fit(X_train, y_train)
    model_pred = knn.predict(X_test)
    mse = mean_squared_error(model_pred, y_test)
    print("Mean squared error: {:.2f}".format(mse))
    for pred, actual in zip(model_pred, y_test):
        print(pred,actual)

def model_knn(destination_path):
    raw = pd.read_csv(WINDOWS_SAMPLE_FILENAME, names = ["User ID", "Gender", "Age", "Occupation", "Star Sign", "date", "text"]).head(10000)
    data = n_grams(raw, N)
    data.to_csv(destination_path)

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

def evaluate_k_nn(training_filepath, testing_filepath):
    train = pd.read_csv(training_filepath)
    #dont want too many test cases ahahaha
    test = pd.read_csv(testing_filepath, names = ["User ID", "Gender", "Age", "Occupation", "Star Sign", "date", "text"]).head(100)
    test_df = convert_n_grams(test, N)
    train, test_df = reconcile(train, test_df)
    train = normalise(train)
    test_df = normalise(test_df)
    # train.to_csv("test.csv", index = False)
    # test_df.to_csv("test2.csv", index = False)
    k_nn(train, test_df)
