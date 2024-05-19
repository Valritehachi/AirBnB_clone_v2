#!/usr/bin/python3
"""
a function that imports webstatic
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """a function that prints hbnb filters."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(excpt=None):
    """a function that does tear down."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
