#!/usr/bin/env python3
""" flask app with Babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _, g
import pytz

app = Flask(__name__)


class Config():
    """babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_TRANSLATION_DICTIONARIES = """/home/steph/alx-backend/
                                      0x02-i18n/translations"""


def get_locale():
    """ function that determines the best language setting
    for the current HTTP request
    """
    url_param = request.args.get("locale", default='en')
    user_locale = g.user.get('locale')
    header_locale = request.headers.get('Accept-Language')

    if url_param and url_param in app.config['LANGUAGES']:
        return url_param
    if g.user and user_locale in app.config['LANGUAGES']:
        return user_locale
    if header_locale and header_locale in app.config['LANGUAGES']:
        return header_locale
    return 'en'


@babel.timezoneselector
def get_timezone():
    """ gets timezone of user"""
    # retrieving timezone from URL or user data
    if request.args.get('timezone'):
        user_timezone = request.args.get('timezone')
    elif g.user.get('timezone'):
        user_timezone = g.user.get('timezone')

    # validating timezone
    try:
        return pytz.timezone(user_timezone)
    except pytz.UnkownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


babel = Babel(app, locale_selector=get_locale)
app.config.from_object('1-app.Config')

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """returns a user dictionary"""
    user_id = request.args.get("login_as")
    if user_id and int(user_id) in users.keys():
        return users[user_id]
    else:
        return None


@app.before_request
def before_request():
    """ finda a user"""
    user = get_user()
    g.user = user


@app.route('/', strict_slashes=False)
def index():
    """ route for index page of flask app """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
