import csv
import json

from contextlib import contextmanager


@contextmanager
def context_manager_for_reformat_file(path_read, path_write):
    try:
        with open(path_read, 'r') as csv_file_open:
            reader = csv.DictReader(csv_file_open)
            rows = list(reader)
        with open(path_write, 'w') as json_file_open:
            json.dump(rows, json_file_open, indent=2)

    except OSError:
        print('File not found or unavailable')
    finally:
        csv_file_open.close()
        json_file_open.close()
        print('Closing files')


@contextmanager
def context_manager_for_correction_file(path_read, path_write):
    try:
        with open(path_read, 'r') as json_file_open:
            reader = json.load(json_file_open)
            rows = list(reader)
        with open(path_write, 'w') as json_file_open:
            json.dump(rows, json_file_open, indent=2)

    except OSError:
        print('File not found or unavailable')
    finally:
        json_file_open.close()
        print('Closing files')


if __name__ == '__main__':
    context_manager_for_reformat_file('books.csv', 'books.json')
    context_manager_for_correction_file('users.json', 'new_users.json')
