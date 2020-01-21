#!/usr/bin/python3
"""Starts a Flask web application:."""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def app_context(abc):
    storage.close()


@app.route('/states', strict_slashes=False)
def all_states():
    states = storage.all('State')
    return render_template('9-states.html', all=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    states = storage.all('State')

    for element in states.values():
        if element.id == id:
            state = element
            return render_template('9-states.html', element=state)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
