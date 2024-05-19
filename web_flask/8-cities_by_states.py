#!/usr/bin/python3
"""
a funtion that Starts up a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def closedb(exc):
    """ a function used to close up the database"""
    storage.close()


@app.route('/cities_by_states')
def states_list():
    """ a function that states the list"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)

if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)