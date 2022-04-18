import matplotlib.pyplot as plt
from flask import request

from src.ui.animal_info import *
from src.ui.user_info import *

predict_blueprint = Blueprint('predict', __name__)


# made function to predict population
def linear_regression_for(x, y):
    sum_Xi = sum(x)
    sum_Yi = sum(y)
    n = x.shape[0]
    m = ((sum_Xi * sum_Yi) - n * sum(x * y)) / (sum_Xi ** 2 - n * sum(x ** 2))
    b = ((sum_Xi * sum(x * y)) - (sum(x ** 2) * sum_Yi)) / ((sum_Xi ** 2) - n * sum(x ** 2))
    print(m, b)
    return m, b


# filter data which come from load_data with specific animal name
def filter_df_for(animal_name, country_name, df):
    return df[(df['Animal'] == animal_name) & (df['Country'] == country_name)]


# read data from csv
def load_data():
    return pd.read_csv('../../data/Population_by_year.csv')


# made rest api
@predict_blueprint.route('/predict', methods=['GET', 'POST'])
def predict_population():
    global pred_y
    animal_name = request.args.get("animal_name")
    name = getMappedName(animal_name)  # take animal name from detection model
    year = request.args.get("years")
    con_name = "world"
    df = load_data()
    if df.shape[0] == 0:
        return render_template("index.html", name=name, users=user_details(), loaded=False, is_plotted=False)
    df = filter_df_for(name, con_name, df)
    if df.shape[0] == 0:
        return render_template("index.html", name=name, users=user_details(), loaded=False, is_plotted=False)
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
    plt.plot(X, Y, label=name)
    plt.legend()
    plt.savefig('../ui/static/plot.png')
    animal_info = get_all_details_for(name)
    return render_template("index.html", name=name, mapped_name=animal_name, users=user_details(), loaded=True,
                           info=animal_info, is_plotted=True, plot_path="static/plot.png")
