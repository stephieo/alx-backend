#!/usr/bin/env python3
""" flask app"""
from flask import Flask, render_template
# from flask_babel import Babel

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ route for index page of flask app """
    return render_template('-index.html')


if __name__ == "__main__":
    app.run(debug=True)
