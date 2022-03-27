import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression

data = pd.read_csv("/Users/sushithks/IdeaProjects/pandas/data/Population_by_year.csv")

animal_data = data.loc[data['Animal'] == 'Rhino(Sumatran)']  # has to be user input
animal_data = animal_data.loc[data['Country'] == 'World']  # has to be user input
animal_data.sort_values("Year")
# print(animal_data)
animal_data = animal_data.reset_index(drop=True)

X = np.array(animal_data)[:, 2].reshape(-1, 1)    # fetching the 3rd column (year)
Y = np.array(animal_data)[:, 3].reshape(-1, 1)    # fetching the 4th column (population)
# print(X)
# print(Y)

animal_data.iloc[0]

predict_year = []
last_ele_array = X[len(X)-1]
last_ele = last_ele_array[0]    # Finding the last year inorder to find out the next years


for i in range (5):
    last_ele = last_ele + 1
    predict_year.append(last_ele)

# print(predict_year)
predict_year= np.array(predict_year).reshape(-1, 1)
regsr = LinearRegression()
regsr.fit(X,Y)

predicted_y = regsr.predict(predict_year)
m = regsr.coef_
c = regsr.intercept_

print("Predicted values :")
for i in range(5):
    print(predict_year[i], "--->", predicted_y[i])

print("slope (m): ", m)
print("y-intercept (c): ", c)