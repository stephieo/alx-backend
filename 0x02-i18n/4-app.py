#!/usr/bin/env python3
""" flask app with Babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

app = Flask(__name__)


def get_locale():
    """ function that determines the best language setting
    for the current HTTP request
    """
    # url_param = request.args.get("locale")
    # if url_param and url_param in app.config['LANGUAGES']:
    #     return url_param
    # else:
    #     return 'fr'
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    return request.args.get('locale', default='en')


babel = Babel(app, locale_selector=get_locale)


class Config():
    """babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_TRANSLATION_DICTIONARIES = """/home/steph/alx-backend/
                                     0x02-i18n/translations"""


app.config.from_object('1-app.Config')


@app.route('/', strict_slashes=False)
def index():
    """ route for index page of flask app """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
