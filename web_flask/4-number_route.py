#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
