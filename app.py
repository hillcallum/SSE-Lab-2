from flask import Flask, render_template, request
from app import process_query

app = Flask(__name__)


@app.route("/", methods=["GET"])
def receive():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    input_color = request.form.get("color")

    result = (
        f"Hello {input_name}! You are {input_age} years old "
        f"and your favourite colour is {input_color}.")
    
    return render_template("result.html", result=result)
