import csv
import json
import random

from contextlib import contextmanager


@contextmanager
def context_manager_for_read_file(path_read):
    try:
        file_open = open(path_read, 'r')
        yield file_open
    except OSError:
        print('File not found or unavailable')
    finally:
        file_open.close()
        print('Closing files')


@contextmanager
def context_manager_for_correction_file(path_write):
    try:
        file_open = open(path_write, 'w')
        yield file_open
    except OSError:
        print('File not found or unavailable')
    finally:
        file_open.close()
        print('Closing files')


if __name__ == '__main__':
    # Читаем из csv книги
    with context_manager_for_read_file('books.csv') as cvs_file_open:
        reader = csv.DictReader(cvs_file_open)
        rows_from_csv = list(reader)
        books = []
        for i in rows_from_csv:
            books.append({'title': i.get('Title'),
                          'author': i.get('Author'),
                          'height': i.get('Height')})

    # Читаем из json юзеров
    with context_manager_for_read_file('users.json') as json_file_open:
        reader = json.load(json_file_open)
        rows_from_json = list(reader)
        users = []
        for i in rows_from_json:
            users.append({'name': i.get('name'),
                          'gender': i.get('gender'),
                          'address': i.get('address'),
                          'books': {}})

    for i in users:
        i['books'] = [random.choice(books) for i in range(2)]

    # Записываем users в json
    with context_manager_for_correction_file('new_users.json') as json_file_open:
        json.dump(users, json_file_open, indent=2)
