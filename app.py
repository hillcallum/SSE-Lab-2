from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def receive():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    
    # Process the data (you can add more logic here if needed)
    result = f"Hello {input_name}! You are {input_age} years old."
    
    # Return the result to a new template or the same template
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
