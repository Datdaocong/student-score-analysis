import pandas as pd
from sklearn.linear_model import LinearRegression

# load dataset
df = pd.read_csv("data/students.csv")

# create average score
df["average"] = (df["math"] + df["english"] + df["science"]) / 3

# features
X = df[["math","english","science"]]

# target
y = df["average"]

# create model
model = LinearRegression()

# train model
model.fit(X, y)

# prediction
prediction = model.predict([[7,8,9]])

print("Predicted average score:", prediction)

'''
ML basic pipeline:
math + english + science
↓
learn relationship
↓
predict average score'''