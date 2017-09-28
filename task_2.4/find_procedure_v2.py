# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

def is_sql_file(filename):
    return os.path.splitext(filename)[1] == '.sql'

# open file into sting
def file_open(path_to_filename):
    with open(path_to_filename) as f:
        file_string = f.read()
    return file_string

# check if search string is in file
def check_search_sting_in_file_sting(search_string, file_string):
    return search_string in file_string

# list of all SQL files with path in search directory
def all_sql_files_paths(dir_for_search):
    all_sql_files_paths_list = []
    for root, dirs, files in os.walk(search_dir):
    # print(type(files))
        for file in files:
            if is_sql_file(file):
                all_sql_files_paths_list.append(os.path.join(root, file))
    return all_sql_files_paths_list

# count search result for substring in sql files
def search_results_count(search_string, files_path_list):
    result_count = 0
    for file_path in files_path_list:
        file_string = file_open(file_path)
        if check_search_sting_in_file_sting(search_string, file_string):
            result_count += 1
    return result_count

# search result list for substring in sql files
def search_results_list(search_string, files_path_list):
    result_list = []
    for file_path in files_path_list:
        file_string = file_open(file_path)
        if check_search_sting_in_file_sting(search_string, file_string):
            result_list.append(file_path)
    return result_list


if __name__ == '__main__':

    search_dir = os.path.join(current_dir, migrations)
    search_list = all_sql_files_paths(search_dir)
    while True:
        search_string = input('Введите строку для поиска:\n')
        search_list = search_results_list(search_string, search_list)
        print('\n'.join(search_list))
        print('Всего: ', search_results_count(search_string, search_list))

    pass