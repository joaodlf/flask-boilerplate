""" Creates an app instance for uwsgi. """
import os

from web.app import create_app

app = create_app(os.getenv("FLASK_CONFIG") or "default")
