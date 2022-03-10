import pandas as pd
from flask import render_template, Blueprint

info_blueprint = Blueprint('info', __name__)


def basic_details():
    return pd.read_csv('../../data/Animal.csv')


def affecting_factors():
    return pd.read_csv('../../data/Effecting_Factor.csv').drop(columns=['Country'])


def endangered_status():
    return pd.read_csv('../../data/Endangered_Species.csv').drop(columns=['Year', 'Extinction_Rate', 'Continent'])


def remediation():
    return pd.read_csv('../../data/Remediation_measures.csv').drop(columns=['Country', 'Effect_of_Measures'])


@info_blueprint.route("/info/")
def info():
    title = "Details of Mammals under threat..."
    df = basic_details()
    return render_template("base.html", title=title, tables=[df.to_html(classes='data', header="true")],
                           titles=df.columns.values)


@info_blueprint.route("/factors")
def factors():
    title = "Factors affecting of existence of Mammals..."
    df = affecting_factors()
    return render_template("base.html", title=title, tables=[df.to_html(classes='data', header="true")],
                           titles=df.columns.values, )


@info_blueprint.route("/status")
def status():
    title = "Endangered Status of Mammals..."
    df = endangered_status()
    return render_template("base.html", title=title, tables=[df.to_html(classes='data', header="true")],
                           titles=df.columns.values)


@info_blueprint.route("/remediation")
def remediation_steps():
    title = "Remediation steps taken to protect these mammals..."
    df = remediation()
    return render_template("base.html", title=title, tables=[df.to_html(classes='data', header='true')],
                           titles=df.columns.values)
