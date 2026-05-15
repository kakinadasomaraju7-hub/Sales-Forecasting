import pandas as pd

df = pd.read_csv("dataset/archive.csv")
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

df.to_csv("dataset/cleaned_data.csv", index=False)