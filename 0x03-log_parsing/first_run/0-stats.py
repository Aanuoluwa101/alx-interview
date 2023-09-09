#!/usr/bin/python3
"""Defines a log parser"""


import sys
import re
check_format = __import__('check_format').check_log_format
parse = __import__('parse').parse
print_dict = __import__('print_dict').print_dict


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
