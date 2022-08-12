#! /usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:expandtab:cuc:autoindent:ignorecase:colorcolumn=99

__author__ = 'Dieter Vansteenwegen'
__email__ = 'github@vansteenwegen.org'

from custom_logging import setup_logging
import logging

log = logging.getLogger()
setup_logging()
for i in range(300):
    if i % 2 == 0:
        log.debug(f'MSG{i:03.0f}: This only goes to log files.')
    else:
        log.warning(
            f'MSG{i:03.0f}: This is a warning, so also goes to stdout.')
