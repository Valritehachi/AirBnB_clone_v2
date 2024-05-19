#!/usr/bin/python3
"""
a function that starts a Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ a function that Prints out the  Web flask."""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ a function that Prints out the  Web flask."""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ a function that Prints out the  Web flask."""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ a function that Prints out the  Web flask."""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ a function that Prints out the  Web flask."""
    return '{} is number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ a function that Prints out the  Web flask."""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ a function that Prints out the  Web flask."""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000)
