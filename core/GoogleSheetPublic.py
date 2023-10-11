import os
import pandas as pd

SHEET_ID=os.environ.get("SHEET_ID")
SHEET_NAME=os.environ.get("SHEET_NAME")

def fetch_data():
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"
    df = pd.read_csv(url)
    data_dict = df.to_dict(orient="records")
    return data_dict
