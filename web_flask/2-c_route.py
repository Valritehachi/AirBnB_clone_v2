#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """a function that prints out the web"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """a function that print web"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """a function that prints out the web route """
    return 'C {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
