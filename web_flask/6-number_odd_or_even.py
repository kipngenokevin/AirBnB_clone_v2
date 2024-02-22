#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Method that returns hello world"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello():
    """This says HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Text to replace objects"""
    text = text.replace('_', ' ')
    return 'C ' + text


@app.route('/python/')
@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    """python is cool!"""
    text = text.replace('_', ' ')
    return 'Python ' + text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """return n only if it is an integer"""
    n = str(n)
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Returns a template"""
    n = str(n)
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    """Returns whether a number is odd or even"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
