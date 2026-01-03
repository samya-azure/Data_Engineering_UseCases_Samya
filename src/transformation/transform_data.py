import pandas as pd

#def transform_sales_data(df: pd.DataFrame) -> pd.DataFrame:
#    print("Transforming data...")

    # Convert date
#    df["OrderDate"] = pd.to_datetime(df["OrderDate"])

    # Business rule: only high value orders
#    df = df[df["Amount"] >= 1000]

    # Add derived column
 #   df["AmountWithTax"] = df["Amount"] * 1.18

 #   return df

def transform_sales_data(df):
    print("🔄 Transforming data...")

    df["OrderDate"] = pd.to_datetime(df["OrderDate"])

    # Explicit copy to avoid SettingWithCopyWarning
    df = df.loc[df["Amount"] >= 1000].copy()

    df.loc[:, "AmountWithTax"] = df["Amount"] * 1.18

    return df
