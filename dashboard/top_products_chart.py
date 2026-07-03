import streamlit as st
import plotly.express as px

def show_top_products_chart(df):

    top_products = (
        df.groupby("Description")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_products,
        x="Revenue",
        y="Description",
        orientation="h",
        title="Top 10 Selling Products"
    )

    fig.update_layout(
        template="plotly_dark",
        yaxis=dict(categoryorder="total ascending"),
        xaxis_title="Revenue (£)",
        yaxis_title=""
    )

    st.plotly_chart(fig, use_container_width=True)