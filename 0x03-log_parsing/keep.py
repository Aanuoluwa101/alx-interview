
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

