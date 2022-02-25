import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('../../data/Animal.csv')
X = df.drop(columns=['Status'])
Y = df['Status']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.15)

model = DecisionTreeClassifier()
model.fit(X_train, Y_train)
Z = model.predict(X_test)

score = accuracy_score(Y_test, Z)
print(score)
