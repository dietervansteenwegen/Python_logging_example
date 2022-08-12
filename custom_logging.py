#! /usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:expandtab:cuc:autoindent:ignorecase:colorcolumn=99

__author__ = 'Dieter Vansteenwegen'
__email__ = 'github@vansteenwegen.org'

import yaml
from logging import config
import logging
import datetime as dt

DATEFMT = '%d/%m/%Y %H:%M:%S'
# For date formatting options see
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes


class MilliSecondsFormatter(logging.Formatter):

    def formatTime(self,
                   record: logging.LogRecord,
                   datefmt: str = DATEFMT) -> str:
        ct: dt.datetime = dt.datetime.fromtimestamp(record.created)
        t: str = ct.strftime(datefmt)
        return f'{t}.{int(record.msecs):03}'


def setup_logging():
    with open('logging_conf.yaml', 'rt') as conf_input:
        conf_data_yaml = yaml.safe_load(conf_input.read())
        config.dictConfig(conf_data_yaml)