#!/usr/bin/python3
"""This script starts a Flask web app"""


ifrom flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Returns hello message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Display C followed by some text"""
    return "C " + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """Display Python followed by some text"""
    return "Python " + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays a number"""
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays a HTML page if n is an int"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
