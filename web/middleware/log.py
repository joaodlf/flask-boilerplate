from logzero import logger


def register(app):
    """ Simple middleware to log all requests. Mostly useful during development.
    This should always be the first middleware to be loaded. """

    @app.before_request
    def before_request():
        logger.info("--- START REQUEST ---")

    @app.after_request
    def after_request(response):
        logger.info("--- END REQUEST ---")
        return response
