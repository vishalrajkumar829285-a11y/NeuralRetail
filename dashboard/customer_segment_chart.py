import streamlit as st
import plotly.express as px

from src.rfm_analysis import rfm_analysis


def show_customer_segmentation_chart(df):

    # RFM Table
    rfm = rfm_analysis(df)

    # Count Segments
    segment_counts = (
        rfm["Segment"]
        .value_counts()
        .reset_index()
    )

    segment_counts.columns = ["Segment", "Customers"]

    fig = px.bar(
        segment_counts,
        x="Segment",
        y="Customers",
        color="Segment",
        title="Customer Segmentation"
    )

    st.plotly_chart(fig, use_container_width=True)