import pandas as pd
from flask import Blueprint
from flask import Flask, request, render_template
from src.ui.animal_info import getMappedName


predict_blueprint = Blueprint('predict', __name__)

#made function to predict population
def linear_regression_for(x, y):
    sum_Xi = sum(x)
    sum_Yi = sum(y)
    n = x.shape[0]
    m = ((sum_Xi * sum_Yi) - n * sum(x * y)) / (sum_Xi ** 2 - n * sum(x ** 2))
    b = ((sum_Xi * sum(x * y)) - (sum(x ** 2) * sum_Yi)) / ((sum_Xi ** 2) - n * sum(x ** 2))
    print(m,b)
    return m, b

#filter data which come from load_data with specific animal name
def filter_df_for(animal_name, df):
    return df[df['Animal'] == animal_name]

#read data from csv
def load_data():
    return pd.read_csv('../../data/Population_by_year.csv')

#made rest api
@predict_blueprint.route('/predict',methods=["GET"])
def predict_population():
    global pred_y
    name = request.args.get("animal_name")      #take animal name from detectection model
    year = request.args.get("years")
    df = load_data()
    df = filter_df_for(name, df)
    X = df['Year']
    Y = df['Population']
    m, b = linear_regression_for(X, Y)
    yr = int(year)
    y_hat = m * yr + b
    pred_y = None
    if y_hat <= 0:
        pred_y = 0
    else:
        pred_y = y_hat
    return str(pred_y)
