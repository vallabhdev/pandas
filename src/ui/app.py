from flask import Flask, render_template

from animal_info import *
from save_file import save_blueprint
from user_info import *

app = Flask(__name__)
app.register_blueprint(save_blueprint)


@app.route("/")
def home():
    users = user_details()
    return render_template("index.html", users=users)


@app.route("/info")
def info():
    title = "Details of Mammals under threat..."
    df = basic_details()
    return render_template("base.html", title=title, tables=[df.to_html(classes='data', header="true")],
                           titles=df.columns.values)


@app.route("/factors")
def factors():
    title = "Factors affecting of existence of Mammals..."
    df = affecting_factors()
    return render_template("base.html", title=title, tables=[df.to_html(classes='data', header="true")],
                           titles=df.columns.values, )


@app.route("/status")
def status():
    title = "Endangered Status of Mammals..."
    df = endangered_status()
    return render_template("base.html", title=title, tables=[df.to_html(classes='data', header="true")],
                           titles=df.columns.values)


@app.route("/remediation")
def remediation_steps():
    title = "Remediation steps taken to protect these mammals..."
    df = remediation()
    return render_template("base.html", title=title, tables=[df.to_html(classes='data', header='true')],
                           titles=df.columns.values)


if __name__ == '__main__':
    app.run(debug=True)
