import pandas as pd
from src.config.settings import RAW_DATA_PATH

def read_sales_data():
    print("Reading raw sales data...")
    df = pd.read_csv(RAW_DATA_PATH)
    return df
