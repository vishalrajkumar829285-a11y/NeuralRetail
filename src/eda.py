import matplotlib.pyplot as plt


def top_selling_products(df):
    # Top 10 selling products
    top_products = (
        df.groupby("Description")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\nTop 10 Selling Products:")
    print(top_products)

    plt.figure(figsize=(12, 6))
    top_products.plot(kind="bar")

    plt.title("Top 10 Selling Products")
    plt.xlabel("Product")
    plt.ylabel("Total Quantity Sold")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()


def country_wise_sales(df):
    # Revenue column
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]

    country_sales = (
        df.groupby("Country")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\nTop 10 Countries by Revenue")
    print(country_sales)

    plt.figure(figsize=(12, 6))
    country_sales.plot(kind="bar")

    plt.title("Top 10 Countries by Revenue")
    plt.xlabel("Country")
    plt.ylabel("Revenue")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

    