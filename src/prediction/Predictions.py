import pandas as pd
from flask import Blueprint

predict_blueprint = Blueprint('predict', __name__)


def linear_regression_for(x, y):
    sum_Xi = sum(x)
    sum_Yi = sum(y)
    n = x.shape[0]
    m = ((sum_Xi * sum_Yi) - n * sum(x * y)) / (sum_Xi ** 2 - n * sum(x ** 2))
    b = ((sum_Xi * sum(x * y)) - (sum(x ** 2) * sum_Yi)) / ((sum_Xi ** 2) - n * sum(x ** 2))
    return m, b


def filter_df_for(animal_name, df):
    return df[df['Animal'] == animal_name]


def load_data():
    return pd.read_csv('../../data/Population_by_year.csv')


@predict_blueprint.route('/predict/<name>/<year>', methods=['GET'])
def predict_population(name, year):
    df = load_data()
    df = filter_df_for(name, df)
    X = df['Year']
    Y = df['Population']
    m, b = linear_regression_for(X, Y)
    yr = int(year)
    y_hat = m * yr + b
    return str(y_hat)
