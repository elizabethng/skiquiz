from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/explore", methods=['GET', 'POST'])
def explore():
    return render_template("explore.html", page_name="Explore Map")


@app.route("/nameQuiz", methods=['GET', 'POST'])
def nameQuiz():
    return render_template("nameQuiz.html", page_name="Run Name Quiz")


@app.route("/locationQuiz", methods=['GET', 'POST'])
def locationQuiz():
    return render_template("locationQuiz.html", page_name="Run Location Quiz")
