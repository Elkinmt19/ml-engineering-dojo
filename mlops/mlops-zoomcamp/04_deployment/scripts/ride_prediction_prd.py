# Built-in imports
import os
import sys
import argparse
from datetime import datetime

# External imports
import pickle
import pandas as pd

# Define some important directories
MODEL_DIR = '.'
DATA_DIR = "https://nyc-tlc.s3.amazonaws.com/trip+data/"

with open(os.path.join(MODEL_DIR,'model.bin'), 'rb') as f_in:
    dv, lr = pickle.load(f_in)

CATEGORICAL = ['PUlocationID', 'DOlocationID']

def read_data(filename:str) -> pd.DataFrame:
    df = pd.read_parquet(filename)
    
    df['duration'] = df["dropOff_datetime"] - df["pickup_datetime"]
    df['duration'] = df["duration"].dt.total_seconds() / 60

    df = df[(df["duration"] >= 1) & (df["duration"] <= 60)]

    df[CATEGORICAL] = df[CATEGORICAL].fillna(-1).astype('int').astype('str')
    
    return df

def predict(df: pd.DataFrame) -> pd.DataFrame:
    dicts = df[CATEGORICAL].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = lr.predict(X_val)

    df_resulted = pd.DataFrame()
    df_resulted['ride_id'] = f'{datetime.today().year:04d}/{datetime.today().month:02d}_' + df.index.astype('str')
    df_resulted["predictions"] = y_pred

    return df_resulted

def save_predictions(df:pd.DataFrame, year:int, month:int) -> None:
    df.to_parquet(
        os.path.join(
            "predictions",
            f"{datetime.today()}-fhv_tripdata_{year}-{int(month):02d}.parquet"
        ),
        engine='pyarrow',
        compression=None,
        index=False
    )

def main():
    arg_fmt = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=arg_fmt,
        description=main.__doc__
    )
    required = parser.add_argument_group('required arguments')
    required.add_argument(
        '-y', '--year', dest='year', required=True,
        help='The year associated to the dataset that is going to be used to make the predictions'
    )
    required.add_argument(
        '-m', '--month', dest='month', required=True, choices=[str(x) for x in range(1,13)],
        help='The month associated to the dataset that is going to be used to make the predictions'
    )

    args = parser.parse_args()

    print("Making the predictions ... ")
    
    try:
        df = read_data(os.path.join(DATA_DIR, f"fhv_tripdata_{args.year}-{int(args.month):02d}.parquet"))
        predictions = predict(df)
        save_predictions(predictions, args.year, args.month)
        print(f"The mean predicted duration is {predictions['predictions'].mean()}")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    sys.exit(main())
