#!/usr/bin/python3
"""Prints a dictionary containing log statistics"""


def print_dict(dic):
    """Prints a formatted dictionary"""
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    print('File size: {}'.format(dic['file_size']))
    for status_code in status_codes:
        if status_code in dic.keys():
            print('{}: {}'.format(status_code, dic[status_code]))
