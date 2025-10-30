from loguru import logger
import json
import sys


class PadelLogger:
    def __init__(
        self, log_file: str = "padel.log", console: bool = True, level: str = "INFO"
    ):
        self.log_file = log_file
        self.console = console
        self.level = level
        self._configure_logger()

    def _json_sink(self, message):
        """Sink function that writes clean JSON logs to file."""
        record = message.record
        log_object = {
            "time": record["time"].strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "level": record["level"].name,
            "message": record["message"],
        }
        log_object.update(record["extra"])
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_object) + "\n")

    def _configure_logger(self):
        logger.remove()
        logger.add(self._json_sink, level=self.level, enqueue=True)

        if self.console:
            logger.add(
                sys.stdout,
                format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
                level=self.level,
            )

        self._logger = logger

    def info(self, message: str = "", **kwargs):
        self._logger.bind(**kwargs).info(message)

    def warning(self, message: str = "", **kwargs):
        self._logger.bind(**kwargs).warning(message)

    def error(self, message: str = "", **kwargs):
        self._logger.bind(**kwargs).error(message)

    def debug(self, message: str = "", **kwargs):
        self._logger.bind(**kwargs).debug(message)

    def critical(self, message: str = "", **kwargs):
        self._logger.bind(**kwargs).critical(message)

    def exception(self, message: str = "", **kwargs):
        self._logger.bind(**kwargs).exception(message)
