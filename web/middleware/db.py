from flask import g

from models import database


def register(app):
    """ Starts a DB connection per request as well as closing said connection on teardown. """

    @app.before_request
    def before_request():
        """ Establishes a DB connection. """
        g.db = database
        g.db.connect()

    @app.teardown_request
    def teardown_request(exception):
        """ Closes the DB connection (if available).
        teardown_request runs under most conditions, including exceptions. """
        db = getattr(g, "db", None)
        if db is not None:
            db.close()
