from src.config.settings import PROCESSED_DATA_PATH, OUTPUT_DATA_PATH

def save_processed_data(df):
    print("Saving processed data...")
    df.to_csv(PROCESSED_DATA_PATH, index=False)

def save_summary(df):
    print("Creating summary...")
    summary = df.groupby("Country")["Amount"].sum().reset_index()
    summary.to_csv(OUTPUT_DATA_PATH, index=False)
