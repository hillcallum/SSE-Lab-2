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
    
    result = f"Hello {input_name}! You are {input_age} years old and your favorite color is {input_color}."
    
    return render_template("result.html", result=result)  # Render results page

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode
