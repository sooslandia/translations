import logging
import logging.handlers
from datetime import datetime


class ExtendedTimeFormatter(logging.Formatter):
    def __init__(self, *args, timezone=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.timezone = timezone

    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created, self.timezone)
        if datefmt:
            s = dt.strftime(datefmt)
        else:
            s = dt.strftime(self.default_time_format)
            if self.default_msec_format:
                s = self.default_msec_format % (s, record.msecs)
        return s.format(ms=record.msecs)


def setup_logging():
    sltt_logger = logging.getLogger("sltt")
    detailed_formatter = ExtendedTimeFormatter(
        "{asctime} - {levelname} - {name}.{funcName} ({lineno})\n{message}",
        style="{",
        datefmt="%H:%M:%S,{ms:03g} %Y-%m-%d",
    )
    sltt_logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter("%(message)s"))
    sltt_logger.addHandler(console_handler)
    file_handler = logging.handlers.RotatingFileHandler(
        "sltt-log.log", encoding="utf-8", maxBytes=10 * 2**20, backupCount=9
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)
    sltt_logger.addHandler(file_handler)
