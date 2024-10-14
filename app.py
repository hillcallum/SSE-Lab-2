from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the main index page
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Route for handling the color selection submission
@app.route("/submit", methods=["GET"])
def submit():
    # Get the 'message' parameter from the URL
    selected_color_message = request.args.get("message")
    
    # Pass the message to the result template
    return render_template("result.html", message=selected_color_message)

if __name__ == "__main__":
    app.run(debug=True)
