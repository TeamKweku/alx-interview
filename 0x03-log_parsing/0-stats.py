#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics
"""
import sys


total_file_size = 0
number_of_lines = 0
status_codes = [200, 301, 400, 401, 404, 403, 405, 500]
status_code_dict = {}


def print_statistics():
    """
    Print the computed statistics including total file size and
    number of lines by status code.
    """
    print("File Size: {}".format(total_file_size))

    for status, count in sorted(status_code_dict.items()):
        print("{}: {}".format(status, count))


try:
    for line in sys.stdin:
        try:
            file_size = int(line.split()[-1])
            total_file_size += file_size

            status_code = int(line.split()[-2])

            if status_code in status_codes:
                if status_code in status_code_dict:
                    status_code_dict[status_code] += 1
                else:
                    status_code_dict[status_code] = 1

            number_of_lines += 1

            if number_of_lines % 10 == 0:
                print_statistics()

        except ValueError:
            pass

except KeyboardInterrupt:
    print_statistics()
