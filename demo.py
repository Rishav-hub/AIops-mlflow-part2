from cmath import e
import os
import mlflow
import argparse
import time
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import numpy as np

def evaluate(actual,pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse,mae,r2

def get_data():
    URL = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    try:
        df = pd.read_csv(URL, sep=";")
        return df
    except Exception as e:
        raise e

def main(alpha, l1_ratio):
    df = get_data()
    train, test = train_test_split(df)

    TARGET = "quality"

    train_x = train.drop([TARGET], axis=1)
    test_x = test.drop([TARGET], axis=1)

    train_y = train[[TARGET]]
    test_y = test[[TARGET]]
    with mlflow.start_run():
        lr_model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
        lr_model.fit(train_x, train_y)
        pred = lr_model.predict(test_x)
        rmse, mae, r2 = evaluate(test_y, pred)
        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)

        print(f"params- alpha: {alpha}, l1_ratio: {l1_ratio}")
        print(f"eval metrics - rmse: {rmse}, mae: {mae}, r2: {r2}")

        mlflow.sklearn.log_model(lr_model, "model")


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--alpha","-a", type=float, default=0.5)
    args.add_argument("--l1_ratio","-l1", type=float, default=0.5)
    parsed_args = args.parse_args()

    # Set the experiment name and run
    main(parsed_args.alpha, parsed_args.l1_ratio)