"""Public API."""


from flask import jsonify
from sqlalchemy import func

from . import app
from .models import UserAgent


@app.route('/')
def get_random_user_agent():
    """
    Return a random user agent string.

    Returns the user agent string as JSON of the form::

        {
          "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36",
        }
    """
    return jsonify(ua=UserAgent.query.order_by(func.random()).first().string)
