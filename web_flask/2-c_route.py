#!/usr/bin/python3
"""This script starts a Flask web app"""


from flask import Flask
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
