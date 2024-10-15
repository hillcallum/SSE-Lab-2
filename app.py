from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def receive():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    
    if not input_name or not input_age:
        result = "Please provide both your name and age."
    else:
        result = f"Hello {input_name}! You are {input_age} years old."
    
    return render_template("result.html", result=result)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
