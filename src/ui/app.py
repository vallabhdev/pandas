import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)


def basic_details():
    return pd.read_csv('../../data/Animal.csv')


def affecting_factors():
    return pd.read_csv('../../data/Effecting_Factor.csv').drop(columns=['Country'])


def endangered_status():
    return pd.read_csv('../../data/Endangered_Species.csv').drop(columns=['Year', 'Extinction_Rate', 'Continent'])


def remediation():
    return pd.read_csv('../../data/Remediation_measures.csv').drop(columns=['Country', 'Effect_of_Measures'])


@app.route("/search/<name>")
def search_by_name(name):
    title = "Search result for {}".format(name)
    df = basic_details()
    df = df[df['Animal_Name'] == name]
    return render_template("index.html", title=title, tables=[df.to_html(classes='data')],
                           titles=df.columns.values)


@app.route("/")
def default():
    title = "Details of Mammals under threat..."
    df = basic_details()
    return render_template("index.html", title=title, tables=[df.to_html(classes='data', header="true")],
                           titles=df.columns.values)


@app.route("/factors")
def factors():
    title = "Factors affecting of existence of Mammals..."
    df = affecting_factors()
    return render_template("index.html", title=title, tables=[df.to_html(classes='data', header="true")],
                           titles=df.columns.values, )


@app.route("/status")
def status():
    title = "Endangered Status of Mammals..."
    df = endangered_status()
    return render_template("index.html", title=title, tables=[df.to_html(classes='data', header="true")],
                           titles=df.columns.values)


@app.route("/remediation")
def remediation_steps():
    title = "Remediation steps taken to protect these mammals..."
    df = remediation()
    return render_template("index.html", title=title, tables=[df.to_html(classes='data', header='true')],
                           titles=df.columns.values)


if __name__ == '__main__':
    app.run(debug=True)
