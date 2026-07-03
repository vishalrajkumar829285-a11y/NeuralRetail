import matplotlib.pyplot as plt
import pandas as pd


def monthly_sales_trend(df):
    # Convert InvoiceDate to datetime
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Create Month-Year column
    df["Month"] = df["InvoiceDate"].dt.to_period("M")

    # Create Revenue column
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]

    # Monthly revenue
    monthly_sales = (
        df.groupby("Month")["Revenue"]
        .sum()
    )

    print("\nMonthly Sales Trend:")
    print(monthly_sales)

    # Plot
    plt.figure(figsize=(12, 6))

    monthly_sales.plot(kind="line", marker="o")

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")

    plt.xticks(rotation=45)

    plt.grid(True)

    plt.tight_layout()
    plt.show()