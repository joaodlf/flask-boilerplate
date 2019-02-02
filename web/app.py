""" Main app module - responsible for bootstrapping the application. """
from flask import Flask, render_template

import config


def create_app(config_name):
    from web.flask_config import flask_config
    app = Flask(__name__, static_folder="static")
    app.config.from_object(flask_config[config_name])

    register_error_handlers(app)
    register_blueprints(app)
    register_middleware(app)

    return app


def register_blueprints(app):
    from web.views import blueprints
    app.register_blueprint(blueprints.public_blueprint)
    app.register_blueprint(blueprints.api_blueprint)

    return None


def register_middleware(app):
    from web import middleware

    if not app.config["TESTING"]:
        middleware.db.register(app)

    return None


def register_error_handlers(app):
    # Sentry.
    if config.SENTRY_DSN:
        import sentry_sdk
        from sentry_sdk.integrations.flask import FlaskIntegration

        sentry_sdk.init(
            dsn=config.SENTRY_DSN,
            integrations=[FlaskIntegration()]
        )

    # HTTP error templates.
    def render_error(error):
        # Render error template. Note that this won't work in DEBUG mode for 500s.
        error_code = getattr(error, "code", 500)
        return render_template(f"errors/{error_code}.html"), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
