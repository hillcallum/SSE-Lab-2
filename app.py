from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def receive():
    return render_template("index.html")  # Render the form

@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")  # Get name from form
    input_age = request.form.get("age")    # Get age from form
    input_color = request.form.get("color")  # Get favorite color from form
    
    # Process the data (you can add more logic here if needed)
    result = f"Hello {input_name}! You are {input_age} years old and your favorite color is {input_color}."
    
    # Return the result to a new template
    return render_template("result.html", result=result)  # Render results page

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode
