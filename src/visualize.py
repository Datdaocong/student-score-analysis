import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/students.csv")

df["average"] = (df["math"] + df["english"] + df["science"]) / 3

plt.bar(df["name"], df["average"])

plt.title("Student Average Scores")
plt.xlabel("Student")
plt.ylabel("Average Score")

plt.savefig("images/average_scores.png")

plt.show()