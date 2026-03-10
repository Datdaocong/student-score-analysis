import pandas as pd

df = pd.read_csv("data/students.csv")

print(df)
print(df.head())

print(df.info())

print(df.describe())

