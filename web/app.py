""" Main app module - responsible for bootstrapping the application. """
from flask import Flask, render_template

import config
from web import flask_config, middleware, views
from web.sentry import sentry


def create_app():
    app = Flask(__name__, static_folder="static")
    app.config.from_object(flask_config.load())

    register_error_handlers(app)
    register_blueprints(app)
    register_middleware(app)

    return app


def register_blueprints(app):
    app.register_blueprint(views.public.blueprint)
    app.register_blueprint(views.api.blueprint)

    return None


def register_middleware(app):
    middleware.log.register(app)
    middleware.db.register(app)

    return None


def register_error_handlers(app):
    if config.SENTRY_DSN:
        sentry.init_app(app)

    # HTTP error templates.
    def render_error(error):
        # Render error template. Note that this won't work in DEBUG mode for 500s.
        error_code = getattr(error, "code", 500)
        return render_template(f"errors/{error_code}.html"), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
