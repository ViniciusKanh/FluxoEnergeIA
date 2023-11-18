
import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def run_data_analysis():
    df = load_data('/path/to/dataset.csv')
    # Adicione aqui as análises, como df.describe(), df.info(), etc.
    return df
