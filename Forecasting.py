import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"C:\Users\VARALAKSHMI KAKINADA\Downloads\archive.zip")

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.month

X = df[['Month']]
y = df['Sales']

model = LinearRegression()
model.fit(X, y)

print("Model trained successfully")