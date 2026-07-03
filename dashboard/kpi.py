import streamlit as st

def show_kpis(df):
    """
    Display KPI cards on the dashboard.
    """

    total_revenue = df["Revenue"].sum()
    total_orders = df["InvoiceNo"].nunique()
    total_customers = df["CustomerID"].nunique()
    avg_order_value = total_revenue / total_orders

    st.subheader("📊 Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="💰 Total Revenue",
            value=f"£{total_revenue:,.2f}"
        )

    with col2:
        st.metric(
            label="🛒 Total Orders",
            value=f"{total_orders:,}"
        )

    with col3:
        st.metric(
            label="👥 Total Customers",
            value=f"{total_customers:,}"
        )

    with col4:
        st.metric(
            label="📦 Avg Order Value",
            value=f"£{avg_order_value:,.2f}"
        )

    st.markdown("---")