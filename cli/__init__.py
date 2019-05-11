import atexit
import logging
import os

import logzero
import pendulum
import sentry_sdk
from logzero import logger
from sentry_sdk import capture_message

from config import SENTRY_DSN
from models.cli import Cli as CliModel


class Cli:
    """The class every CLI job should inherit from.
        It creates/updates a cron entry in the database; manages the log file; ensures there aren't duplicate processes running."""

    def __init__(self, name):
        self.pid = os.getpid()
        self.name = name
        self.cron_db_entry = None
        self.logs_dir = "cli/logs"
        if SENTRY_DSN:
            sentry_sdk.init(SENTRY_DSN)

        # Set the logger.
        logzero.loglevel(logging.INFO)
        logzero.logfile(
            f"{self.logs_dir}/{self.name}.log", maxBytes=1000000, backupCount=3
        )

        # Execute finish() at the end of CLI execution.
        atexit.register(self._finish)

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
                    capture_message(
                        f"Process #{cron_db_entry.pid} ({cron_db_entry.name}) is still running!",
                        level="error",
                    )
                else:
                    logger.error(error)

                exit(1)
        except CliModel.DoesNotExist:
            # First time running.
            logger.info(f"Adding new cron {self.name}")
            cron_db_entry = CliModel.create(name=self.name)

        cron_db_entry.pid = self.pid
        cron_db_entry.dt_start = pendulum.now()
        cron_db_entry.dt_finish = None

        self.cron_db_entry = cron_db_entry
        self.cron_db_entry.save()

        logger.info("--- STARTING ---")
        logger.info(f"--- Logging to {self.logs_dir}/{self.name}.log ---")

    def _finish(self):
        """Called at the end of execution."""
        self.cron_db_entry.dt_finish = pendulum.now()
        self.cron_db_entry.save()
        logger.info("--- FINISHING ---")
