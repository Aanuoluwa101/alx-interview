#!/usr/bin/python3
"""Checks a log string for conformation to a specified pattern"""


import re


def check_log_format(log_string):
    """Checks log string's format"""
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] \"GET /projects/260 HTTP/1\.1" \d+ \d+$'
    return re.match(pattern, log_string) is not None
