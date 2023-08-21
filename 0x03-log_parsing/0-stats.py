#!/usr/bin/python3
"""Defines a log parser"""


import sys
import re
# check_format = __import__('check_format').check_log_format
# parse = __import__('parse').parse
# print_dict = __import__('print_dict').print_dict


def check_log_format(log_string):
    """Checks log string's format"""
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] \
               "GET /projects/260 HTTP/1\.1" \d+ \d+$'
    return re.match(pattern, log_string) is not None


def parse(log_string):
    """Returns the status code and file size"""
    file_size, status_code = log_string.split(' ')[-1:-3:-1]
    return status_code, file_size


def print_dict(dic):
    """Prints a formatted dictionary"""
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    print('File size: {}'.format(dic['file_size']))
    for status_code in status_codes:
        if status_code in dic.keys():
            print('{}: {}'.format(status_code, dic[status_code]))


def log_parser():
    """Parses logs from stdin and prints statistics of thesame
       at intervals or on keyboard interrupt"""
    dc = {'file_size': 0}
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    try:
        while True:
            count = 1
            for line in sys.stdin:
                if check_format(line):
                    try:
                        status_code, file_size = [int(x) for x in parse(line)]
                        if status_code in status_codes:
                            if status_code not in dc:
                                dc[status_code] = 1
                            else:
                                dc[status_code] += 1
                            dc['file_size'] += file_size
                    except ValueError:
                        continue
                if count % 10 == 0:
                    print_dict(dc)
                count += 1
    except KeyboardInterrupt as e:
        print_dict(dc)
        raise e


log_parser()
