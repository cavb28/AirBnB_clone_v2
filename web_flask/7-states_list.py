#!/usr/bin/python3
"""Starts a Flask web application:."""
from flask import Flask, render_template
import os
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def p_route(text):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_template(n):
    if n % 2 == 0:
        data = "even"
    else:
        data = "odd"
    return render_template('6-number_odd_or_even.html', n=n, data=data)


@app.route('/states_list', strict_slashes=False)
def states_list():
    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        from models.engine.db_storage import DBStorage
        storage = DBStorage()
        storage.all(State)
    else:
        from models.engine.file_storage import FileStorage
        storage = FileStorage()
        storage.all(State)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
