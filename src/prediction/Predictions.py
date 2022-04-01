import pandas as pd
from flask import Blueprint
from flask import Flask, request, render_template
import json
import plotly
import plotly.express as px


predict_blueprint = Blueprint('predict', __name__)


def linear_regression_for(x, y):
    sum_Xi = sum(x)
    sum_Yi = sum(y)
    n = x.shape[0]
    m = ((sum_Xi * sum_Yi) - n * sum(x * y)) / (sum_Xi ** 2 - n * sum(x ** 2))
    b = ((sum_Xi * sum(x * y)) - (sum(x ** 2) * sum_Yi)) / ((sum_Xi ** 2) - n * sum(x ** 2))
    print(m,b)
    return m, b


def filter_df_for(animal_name, df):
    return df[df['Animal'] == animal_name]


def load_data():
    return pd.read_csv('../../data/Population_by_year.csv')

@predict_blueprint.route('/predict',methods=["GET","POST"])
def predict_population():
    global pred_y
    name = request.args.get("animal_name")
    year = request.args.get("year")
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
    result = pd.data
    fig = px.line(X,Y)
    return str(pred_y)
