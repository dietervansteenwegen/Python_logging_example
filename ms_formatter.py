import logging
import datetime as dt

DATEFMT = '%d/%m/%Y %H:%M:%S'  # See https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes


class MilliSecondsFormatter(logging.Formatter):

    def formatTime(self,
                   record: logging.LogRecord,
                   datefmt: str = DATEFMT) -> str:
        ct: dt.datetime = dt.datetime.fromtimestamp(record.created)
        t: str = ct.strftime(datefmt)
        return f'{t}.{int(record.msecs):03}'
