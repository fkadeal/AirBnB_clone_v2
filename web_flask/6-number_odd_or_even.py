#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text variable
    /python/<text>: display 'Python' followed by the value of the text variable
    The default value of text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
    /number_odd_or_even/<n>: display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
"""
from flask import Flask
from flask import render_template

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


@app.route("/number_template/<int:n>", strict_slashes=False)
def param_number(n):
    """ Displays 'value of text' """
    return render_template('5-number.html', title='number is', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def param_numberCheck(n):
    """ Displays 'if number value is even or odd' """
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, isit='even')
    elif n % 2 != 0:
        return render_template('6-number_odd_or_even.html', n=n, isit='odd')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
