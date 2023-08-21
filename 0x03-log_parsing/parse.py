#!/usr/bin/python3
"""Parses the log string
   and extracts the status code and file size"""


def parse(log_string):
    """Returns the status code and file size"""
    file_size, status_code = log_string.split(' ')[-1:-3:-1]
    return status_code, file_size
