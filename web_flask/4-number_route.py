#!/usr/bin/python3
""" a function that starts up a web flask application"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ a function that Prints in the Web """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ a function that Prints in the Web """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ a function that Prints in the Web """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ a function that Prints in the Web """
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
