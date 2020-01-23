#!/usr/bin/python3
"""Starts a Flask web application:."""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def app_context(abc):
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    print(places)
    return render_template('100-hbnb.html', data=states, amen=amenities, place=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
