__author__ = 'ariell'

# Import the Flask class from the Flask module
from flask import Flask

# Create the application object
app = Flask(__name__)

# Error Handling
app.config["DEBUG"] = True

# Use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# Define the view using a function, which returns a string
def hello_world():
    return "Hello, World!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

# integer route
@app.route("/integer/<int:value>")
def int_value(value):
    print value + 1
    return "correct"

# float value
@app.route("/float/<float:value>")
def float_value(value):
    print value + 1
    return "correct"

# dynamic route that accept slashes
@app.route("/path/<path:value>")
def path_value(value):
    print value
    return "correct"

# name view
@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael" :
        return "Hello, {}".format(name), 200
    else :
        return "Not Found", 404

# Start the development server using the run() method
if __name__ == "__main__":
    app.run()
