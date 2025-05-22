import pandas as pd

def load_and_clean_data(file):
    df = pd.read_csv(file)
    df.dropna(axis=0, inplace=True)
    return df

def summarize_dataset(df):
    return {
        "num_rows": len(df),
        "num_columns": len(df.columns),
        "columns": list(df.columns),
        "basic_stats": df.describe(include='all').to_dict()
    }
