#!/usr/bin/python3
"""import class Flask, render_template method"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays (str) text
    on browser """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ displays (str) text
    on browser """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """displays (str) text
    on browser
    """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """displays (str) text
    on browser
    """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def display_num(n):
    """displays (int) number
    on browser
    """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_HTML(n):
    """displays (int) number
    on browser
    Returns:
        HTML Page
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_odd_even(n):
    """displays (int) number
    on browser
    Returns:
        HTML Page
    """
    if n % 2 == 0:
        desc = 'even'
    else:
        desc = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, desc=desc)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
