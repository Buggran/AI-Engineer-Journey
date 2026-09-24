import pandas as pd


def get_comments(file_path):
    df = pd.read_csv(file_path)

    comments = (
        df["Comment"]
        .dropna()
        .astype(str)
        .tolist()
    )

    return comments