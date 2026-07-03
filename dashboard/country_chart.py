import streamlit as st
import plotly.express as px


def show_country_chart(df):

    country_sales = (
        df.groupby("Country")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        country_sales,
        x="Country",
        y="Revenue",
        color="Revenue",
        title="Top 10 Countries by Revenue"
    )

    st.plotly_chart(fig, use_container_width=True)