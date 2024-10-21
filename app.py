from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def receive():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    input_color = request.form.get("color")

    result = f"Hello {input_name}!"
    f"You are {input_age} years old and your favorite color is {input_color}."

    return render_template("result.html", result=result)


def process_query(query):
    if query.lower() == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    else:
        return "Unknown"


@app.route("/query", methods=["GET"])
def query():
    query_param = request.args.get("q")

    result = process_query(query_param)

    return result


if __name__ == "__main__":
    app.run(debug=True)
