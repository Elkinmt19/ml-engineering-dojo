# Built-in imports
import os
import sys
import datetime
from typing import Union, Any
from dateutil.relativedelta import relativedelta

# External imports
import mlflow
import pickle
import pandas as pd
from prefect import flow, task, get_run_logger
from sklearn.metrics import mean_squared_error
from prefect.deployments import DeploymentSpec
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction import DictVectorizer
from prefect.flow_runners import SubprocessFlowRunner
from prefect.task_runners import SequentialTaskRunner
from prefect.orion.schemas.schedules import CronSchedule

# Own imports
from scripts import get_path_dir as gpd

# Define the path of the data directory
DATA_DIR = gpd.get_desired_folder_path("data")
ARTIFACTS_DIR = os.path.join(DATA_DIR, "../03-orchestration/artifacts")

# Define variables associate with MLflow
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("linear-regression-prefect-workflow")

def dump_pickle(obj: Any, filename: str) -> Any:
    with open(filename, "wb") as f_out:
        return pickle.dump(obj, f_out)

@task
def get_paths(date: str = None) -> Union[str, str]:
    logger = get_run_logger()

    date_buff = datetime.date.today() if (date is None) else datetime.date.fromisoformat(date)

    logger.info("Getting the train and validation datasets")

    train_path = os.path.join(
        DATA_DIR,
        f"fhv_tripdata_{str(date_buff - relativedelta(months=2))[:-3]}.parquet"
    )
    val_path = os.path.join(
        DATA_DIR,
        f"fhv_tripdata_{str(date_buff - relativedelta(months=1))[:-3]}.parquet"
    )

    return train_path, val_path

@task
def read_data(path:str) -> pd.DataFrame:
    df = pd.read_parquet(path)
    return df

@task
def prepare_features(df:pd.DataFrame, categorical:str, train=True) -> pd.DataFrame:
    logger = get_run_logger()

    df['duration'] = df.dropOff_datetime - df.pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60
    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    mean_duration = df.duration.mean()
    if train:
        logger.info(f"The mean duration of training is {mean_duration}")
    else:
        logger.info(f"The mean duration of validation is {mean_duration}")
    
    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    return df

@task
def train_model(df:pd.DataFrame, categorical:str) -> Union[LinearRegression, DictVectorizer, float]:
    logger = get_run_logger()

    train_dicts = df[categorical].to_dict(orient='records')
    dv = DictVectorizer()
    X_train = dv.fit_transform(train_dicts) 
    y_train = df.duration.values

    logger.info(f"The shape of X_train is {X_train.shape}")
    logger.info(f"The DictVectorizer has {len(dv.feature_names_)} features")

    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_pred = lr.predict(X_train)
    rmse = mean_squared_error(y_train, y_pred, squared=False)
    logger.info(f"The RMSE of training is: {rmse}")

    return lr, dv, rmse

@task
def run_model(df:pd.DataFrame, categorical:str, dv:DictVectorizer, lr:LinearRegression) -> Union[bool, float]:
    logger = get_run_logger()

    val_dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(val_dicts) 
    y_pred = lr.predict(X_val)
    y_val = df.duration.values

    rmse = mean_squared_error(y_val, y_pred, squared=False)
    logger.info(f"The RMSE of validation is: {rmse}")

    return True, rmse

@flow(task_runner=SequentialTaskRunner())
def main(date: str) -> None:
    with mlflow.start_run():
        mlflow.set_tag("model", f"linear-regression-{date}")

        train_path, val_path = get_paths(date).result()

        categorical = ['PUlocationID', 'DOlocationID']

        df_train = read_data(train_path)
        df_train_processed = prepare_features(df_train, categorical)
        df_val = read_data(val_path)
        df_val_processed = prepare_features(df_val, categorical, False)

        # train the model
        lr, dv, train_rmse = train_model(df_train_processed, categorical).result()
        _ ,val_rmse = run_model(df_val_processed, categorical, dv, lr).result()

        dump_pickle(dv, os.path.join(ARTIFACTS_DIR, f"dv-{date}.pkl"))
        dump_pickle(lr, os.path.join(ARTIFACTS_DIR, f"model-{date}.pkl"))

        mlflow.log_metrics({"train-rmse": train_rmse, "val-rmse": val_rmse})
        mlflow.log_artifact(local_path=os.path.join(ARTIFACTS_DIR, f"dv-{date}.pkl"), artifact_path="models")
        mlflow.log_artifact(local_path=os.path.join(ARTIFACTS_DIR, f"model-{date}.pkl"), artifact_path="models")

DeploymentSpec(
flow=main,
name="model_training",
schedule=CronSchedule(
    cron="0 9 15 * *",
    timezone="America/Bogota"
),
flow_runner=SubprocessFlowRunner(),
tags=["ml-cron-job"]
)