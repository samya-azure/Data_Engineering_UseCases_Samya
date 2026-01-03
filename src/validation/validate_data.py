def validate_sales_data(df):
    print("Validating data...")

    if df.empty:
        raise ValueError("DataFrame is empty after transformation")

    if df["Amount"].isnull().any():
        raise ValueError("Amount column contains NULL values")

    print("✔ Data validation passed")
