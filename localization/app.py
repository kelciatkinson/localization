#!/usr/bin/env python3
from flask_babel import Babel, _, get_locale
from flask import Flask, request

"""
"""
app = Flask(__name__)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'


babel = Babel(app)

def get_locale():
    return request.accept_languages.best_match(['en', 'fr'])

babel.init_app(app, locale_selector=get_locale)

@app.route('/')
def index():
    locale = get_locale()
    return _("Hello, World!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
