import pandas as pd





df = pd.read_csv(r"C:\Users\VARALAKSHMI KAKINADA\Desktop\VARA LAKSHMI\dataset.csv")
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)


df.to_csv(r"C:\Users\VARALAKSHMI KAKINADA\Desktop\VARA LAKSHMI\dataset.csv", index=False)