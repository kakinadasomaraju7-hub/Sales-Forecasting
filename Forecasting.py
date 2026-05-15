# ---------------- IMPORT LIBRARIES ----------------
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# ---------------- LOAD DATA ----------------
df = pd.read_csv(r"C:\Users\VARALAKSHMI KAKINADA\Desktop\VARA LAKSHMI\dataset.csv")

# ---------------- DATA PREPROCESSING ----------------
# Convert to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Sort data
df = df.sort_values('Order Date')

# Create time-based feature
df['Days'] = (df['Order Date'] - df['Order Date'].min()).dt.days

# ---------------- PREPARE DATA ----------------
X = df[['Days']]   # Feature
y = df['Sales']    # Target

# ---------------- TRAIN MODEL ----------------
model = LinearRegression()
model.fit(X, y)

print("✅ Model trained successfully")

# ---------------- FORECAST FUTURE ----------------
# Create next 30 days
future_days = pd.DataFrame({
    'Days': np.arange(df['Days'].max(), df['Days'].max() + 30)
})

# Predict
future_sales = model.predict(future_days)

# Create future dates
future_dates = pd.date_range(start=df['Order Date'].max(), periods=30)

# Store results
forecast_df = pd.DataFrame({
    'Date': future_dates,
    'Forecast Sales': future_sales
})

print("\n📊 Forecast Data:")
print(forecast_df.head())

# ---------------- VISUALIZATION ----------------
plt.figure(figsize=(10,5))

# Actual sales
plt.plot(df['Order Date'], df['Sales'], label='Actual Sales', color='blue')

# Forecast sales
plt.plot(forecast_df['Date'], forecast_df['Forecast Sales'], label='Forecast', color='red')

# Labels
plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Sales Forecast (Next 30 Days)")
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

# Show graph
plt.show()