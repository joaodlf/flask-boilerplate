import atexit
import logging
import os

import arrow
import logzero
from logzero import logger
from raven import Client

from config import SENTRY_DSN
from models.cli import Cli as CliModel


class Cli:
    """ The class every CLI job should inherit from. """

    def __init__(self):
        self.pid = os.getpid()
        self.name = None
        self.cron_db_entry = None
        self.logs_dir = "cli/logs"

        if SENTRY_DSN:
            self.sentry_client = Client(SENTRY_DSN)

    def start(self, name):
        """CLI initializer, this must always be run at the very start of execution."""
        self.name = name

        # Set the logger.
        logzero.loglevel(logging.INFO)
        logzero.logfile(f"{self.logs_dir}/{self.name}.log", maxBytes=1000000, backupCount=3)

        # Execute finish() at the end of CLI execution.
        atexit.register(self.finish)

        try:
            # Check if the cron entry exists.
            cron_db_entry = CliModel.select().where(CliModel.name == self.name).get()

            try:
                # This doesn't actually kill the process, just sends a signal of 0 to test it.
                os.kill(cron_db_entry.pid, 0)
            except ProcessLookupError:
                # Process does not exist, good to go.
                pass
            else:
                # Process still exists, stop execution!
                error = f"Process #{cron_db_entry.pid} ({cron_db_entry.name}) is still running!"

                if SENTRY_DSN:
                    self.sentry_capture_mesage(f"Process #{cron_db_entry.pid} ({cron_db_entry.name}) is still running!",
                                               level="error")
                else:
                    logger.error(error)

                exit(1)
        except CliModel.DoesNotExist:
            # First time running.
            logger.info(f"Adding new cron {self.name}")
            cron_db_entry = CliModel.create(name=self.name)

        cron_db_entry.pid = self.pid
        cron_db_entry.dt_start = arrow.now().datetime
        cron_db_entry.dt_finish = None

        self.cron_db_entry = cron_db_entry
        self.cron_db_entry.save()

        logger.info("--- STARTING ---")
        logger.info(f"--- Logging to {self.logs_dir}/{self.name}.log ---")

    def finish(self):
        self.cron_db_entry.dt_finish = arrow.now().datetime
        self.cron_db_entry.save()
        logger.info("--- FINISHING ---")

    def sentry_capture_mesage(self, message, level=None):
        """Sends a message to Sentry (as well as logging the message with the specified log level)."""
        if not level:
            level = "info"

        if self.sentry_client:
            self.sentry_client.captureMessage(message)
        else:
            logger.warn("Sentry is not available!")
            if level == "info":
                logger.info(message)
            if level == "error":
                logger.error(message)
