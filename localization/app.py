#!/usr/bin/env python3
from babel import Babel, _
"""
"""

app = Flask(__name__)
babel = Babel(app)


greeting = _("Hello, World!")

if __name__ == "__main__":
    app.run
