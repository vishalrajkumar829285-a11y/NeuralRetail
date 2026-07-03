import pandas as pd


def feature_engineering(df):
    print("\n==============================")
    print("FEATURE ENGINEERING")
    print("==============================")

       # Fix StockCode data type
    df["StockCode"] = df["StockCode"].astype(str)

    # Revenue
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]

    # Invoice Date ko datetime me convert
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # New Features
    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month
    df["Day"] = df["InvoiceDate"].dt.day
    df["Hour"] = df["InvoiceDate"].dt.hour
    df["Weekday"] = df["InvoiceDate"].dt.day_name()

    print("\nNew Features Added Successfully!")

    print("\nColumns:")
    print(df.columns)

    print("\nFirst 5 Rows:")
    print(df.head())

    return df