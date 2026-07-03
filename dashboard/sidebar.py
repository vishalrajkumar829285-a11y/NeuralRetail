import streamlit as st

def show_sidebar(df):

    st.sidebar.header("📊 Dashboard Filters")

    countries = ["All"] + sorted(df["Country"].dropna().unique().tolist())

    selected_country = st.sidebar.selectbox(
        "Select Country",
        countries
    )

    years = ["All"] + sorted(df["Year"].unique().tolist())

    selected_year = st.sidebar.selectbox(
        "Select Year",
        years
    )

    return selected_country, selected_year