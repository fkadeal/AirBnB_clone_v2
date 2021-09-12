#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB' """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def param_c(text):
    """ Displays 'value of text' """
    return "C " + text.replace("_", " ")


@app.route("/python/", defaults={'text': "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def param_python(text):
    """ Displays 'value of text' """
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def param_number(n):
    """ Displays 'value of text' """
    return "{} is number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
