import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd

from src.data_cleaning import clean_data
from src.feature_engineering import feature_engineering

from dashboard.sidebar import show_sidebar
from dashboard.kpi import show_kpis
from dashboard.monthly_sales_chart import show_monthly_sales_chart
from dashboard.top_products_chart import show_top_products_chart
from dashboard.country_chart import show_country_chart
from dashboard.customer_segment_chart import show_customer_segmentation_chart


# Page Config
st.set_page_config(
    page_title="NeuralRetail Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("🛍️ NeuralRetail Dashboard")
st.write("Online Retail Sales Analytics")


# Load Data
file_path = "data/Online Retail.xlsx"

df = clean_data(file_path)
df = feature_engineering(df)

st.success("Data Loaded Successfully!")


# Sidebar
selected_country, selected_year = show_sidebar(df)


# KPI Cards
show_kpis(df)


# ---------------- First Row ----------------
col1, col2 = st.columns(2)

with col1:
    show_monthly_sales_chart(df)

with col2:
    show_top_products_chart(df)


# ---------------- Second Row ----------------
col3, col4 = st.columns(2)

with col3:
    show_customer_segmentation_chart(df)

with col4:
    show_country_chart(df)


# ---------------- Dataset ----------------
with st.expander("📄 Dataset Preview"):
    st.dataframe(df.head())