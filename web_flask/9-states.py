#!/usr/bin/python3
"""
a function that Starts up a Flask web application.
"""
from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """a webflask list states function"""
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """a webflask list states id function"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")

@app.teardown_appcontext
def teardown(exc):
    """a webflask tear down function"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
