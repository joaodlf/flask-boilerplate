import config


class Config(object):
    DEBUG = False
    TESTING = False
    PRODUCTION = False
    SENTRY_DSN = config.SENTRY_DSN
    SECRET_KEY = config.FLASK_SECRET_KEY


class ProductionConfig(Config):
    DEBUG = False
    PRODUCTION = True


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    """ Unit Testing. """
    DEBUG = True
    TESTING = True


flask_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig
}
