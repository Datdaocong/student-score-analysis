import pandas as pd

df = pd.read_csv("data/students.csv")

'''print(df)
print(df.head())

print(df.info())

print(df.describe())

df['average'] = (df['math'] + df['english'] + df['science']) / 3
print(df)'''

def classify(score):
    if score >= 8:
        return "Excellent"
    elif score >= 6.5:
        return "Good"
    else:
        return "Average"

df["grade"] = df["average"].apply(classify)

#print(df)

top_student = df[df["average"] == df["average"].max()]

'''print("Top student:")
print(top_student)'''