#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ function that prints the hbnb hello"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ function that prints the hbnb value"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
