import pandas as pd


def rfm_analysis(df):
    print("\n" + "=" * 50)
    print("RFM ANALYSIS")
    print("=" * 50)

    # Ensure InvoiceDate is datetime
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Reference date
    snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

    # Revenue column
    if "Revenue" not in df.columns:
        df["Revenue"] = df["Quantity"] * df["UnitPrice"]

    # Create RFM Table
    rfm = df.groupby("CustomerID").agg({
        "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
        "InvoiceNo": "nunique",
        "Revenue": "sum"
    })

    rfm.columns = ["Recency", "Frequency", "Monetary"]

    print("\nFirst 10 Customers:\n")
    print(rfm.head(10))

    print("\nRFM Summary:\n")
    print(rfm.describe())

    # Customer Segmentation
    rfm = rfm_segmentation(rfm)

    return rfm


def rfm_segmentation(rfm):
    print("\n" + "=" * 50)
    print("CUSTOMER SEGMENTATION")
    print("=" * 50)

    # R Score (Low Recency = Better)
    rfm["R_Score"] = pd.qcut(
        rfm["Recency"],
        4,
        labels=[4, 3, 2, 1]
    ).astype(int)

    # F Score
    rfm["F_Score"] = pd.qcut(
        rfm["Frequency"].rank(method="first"),
        4,
        labels=[1, 2, 3, 4]
    ).astype(int)

    # M Score
    rfm["M_Score"] = pd.qcut(
        rfm["Monetary"],
        4,
        labels=[1, 2, 3, 4]
    ).astype(int)

    # Combined Score
    rfm["RFM_Score"] = (
        rfm["R_Score"].astype(str)
        + rfm["F_Score"].astype(str)
        + rfm["M_Score"].astype(str)
    )

    # Customer Segments
    def segment(row):
        if row["R_Score"] == 4 and row["F_Score"] == 4:
            return "Champions"
        elif row["F_Score"] >= 3:
            return "Loyal Customers"
        elif row["R_Score"] >= 3:
            return "Potential Loyalists"
        elif row["R_Score"] == 2:
            return "At Risk"
        else:
            return "Lost Customers"

    rfm["Segment"] = rfm.apply(segment, axis=1)

    print("\nCustomer Segments:\n")
    print(rfm["Segment"].value_counts())

    return rfm