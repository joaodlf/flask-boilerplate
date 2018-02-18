from raven.contrib.flask import Sentry
from config import SENTRY_DSN

sentry = Sentry(dsn=SENTRY_DSN)