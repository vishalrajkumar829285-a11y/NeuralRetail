import streamlit as st
import plotly.express as px

def show_monthly_sales_chart(df):

    monthly_sales = (
        df.groupby("Month")["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        monthly_sales,
        x="Month",
        y="Revenue",
        markers=True,
        title="Monthly Sales Trend"
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Revenue (£)",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)