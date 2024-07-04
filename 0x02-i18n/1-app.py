#!/usr/bin/env python3
""" flask app with Babel setup"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('1-app.Config')


@app.route('/', strict_slashes=False)
def index():
    """ route for index page of flask app """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
