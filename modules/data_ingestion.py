import pandas as pd


def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df


def read_json_file(file_path):
    df = pd.read_json(file_path)
    return df