#!/usr/bin/python3
"""
a function that starts a Flask web application
"""

from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """this function that returns Hello HBNB!"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """a function that returns hbnb"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """a function that displays the word c is fun"""
    text = text.replace("_", " ")
    return "C {}".format(text)

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """a function that displays the text python is cool """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """a function that Displays a HTML page when n is an integer."""
    return render_template("5-number.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
