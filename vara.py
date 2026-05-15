import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# ---------------- LOAD DATA ----------------
df = pd.read_csv(r"C:\Users\VARALAKSHMI KAKINADA\Desktop\VARA LAKSHMI\dataset.csv")

# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# ---------------- TITLE ----------------
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Sales & Demand Forecast Dashboard</h1>", unsafe_allow_html=True)

# ---------------- KPI CARDS ----------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"{df['Sales'].sum():,.0f}")
col2.metric("Average Sales", f"{df['Sales'].mean():.2f}")
col3.metric("Max Sales", f"{df['Sales'].max():,.0f}")

# ---------------- FILTER ----------------
st.sidebar.header("Filters")

df['Month'] = df['Order Date'].dt.month
selected_month = st.sidebar.selectbox("Select Month", sorted(df['Month'].unique()))

filtered_df = df[df['Month'] == selected_month]

# ---------------- SALES TREND ----------------
daily_sales = filtered_df.groupby('Order Date')['Sales'].sum().reset_index()

# ---------------- MONTHLY DEMAND ----------------
monthly = df.groupby('Month')['Sales'].sum()

# ---------------- LAYOUT (2 COLUMNS) ----------------
col1, col2 = st.columns(2)

# Sales Trend
with col1:
    st.subheader("Sales Trend")
    fig, ax = plt.subplots()
    ax.plot(daily_sales['Order Date'], daily_sales['Sales'], color='blue')
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Monthly Demand
with col2:
    st.subheader("Monthly Demand")
    st.bar_chart(monthly)

# ---------------- TOP PRODUCTS ----------------
if 'Product Name' in df.columns:
    st.subheader("Top Selling Products")
    top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)
    st.bar_chart(top_products)

# ---------------- FORECAST ----------------
st.subheader("Sales Forecast (Next 30 Days)")

df = df.sort_values('Order Date')
df['Days'] = (df['Order Date'] - df['Order Date'].min()).dt.days

X = df[['Days']]
y = df['Sales']

model = LinearRegression()
model.fit(X, y)

# Future prediction
future_days = np.arange(df['Days'].max(), df['Days'].max() + 30).reshape(-1, 1)
future_sales = model.predict(future_days)

# Future dates
future_dates = pd.date_range(start=df['Order Date'].max(), periods=30)

forecast_df = pd.DataFrame({
    'Date': future_dates,
    'Forecast Sales': future_sales
})

# Forecast Plot
fig2, ax2 = plt.subplots()

ax2.plot(df['Order Date'], df['Sales'], label='Actual', color='green')
ax2.plot(forecast_df['Date'], forecast_df['Forecast Sales'], label='Forecast', color='red')

ax2.set_xlabel("Date")
ax2.set_ylabel("Sales")
ax2.legend()

plt.xticks(rotation=45)
st.pyplot(fig2)