from src.data_cleaning import clean_data
from src.eda import top_selling_products, country_wise_sales
from src.monthly_sales import monthly_sales_trend
from src.feature_engineering import feature_engineering
from src.rfm_analysis import rfm_analysis
from src.customer_segmentation import customer_segmentation_chart


def main():
    file_path = "data/Online Retail.xlsx"

    # Data Cleaning
    df = clean_data(file_path)

    # EDA
    top_selling_products(df)
    country_wise_sales(df)
    monthly_sales_trend(df)

    # Feature Engineering
    df = feature_engineering(df)

    # RFM Analysis + Segmentation
    rfm = rfm_analysis(df)

    # Bar Chart
    customer_segmentation_chart(rfm)


if __name__ == "__main__":
    main()