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

# migrations = 'Migrations'
# current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
	
	# check if file is *.sgl
	def is_sql_file(filename):
		if os.path.splitext(filename)[1] == '.sql':
			result = True
		else:
			result = False
		return result
	
	# open file into sting
	def file_open(path_to_filename):
		with open(path_to_filename) as f:
			file_string = f.read()
		return file_string
	
	# check if search string is in file
	def check_search_sting_in_file_sting(search_string, file_string):
		if search_string in file_string:
			result = True
		else:
			result = False
		return result
	
	# list of all files with path in working directory 1 level subfolders 
	def all_files_paths():
		all_files_paths_list = []
		subdir_1_list = []
		for file_or_dir in os.listdir():
			if os.path.isfile(file_or_dir) == True:
				all_files_paths_list.append(file_or_dir)
			else:
				subdir_1_list.append(file_or_dir)
		for subdir in subdir_1_list:
			for file_or_dir in os.listdir(subdir):
				if os.path.isfile(os.path.join(subdir,file_or_dir)) == True:
					all_files_paths_list.append(os.path.join(subdir,file_or_dir))
		return all_files_paths_list
	
	
	# print search result for substring in sql files
	def search_results_print(search_string, files_path_list):
		for file_path in files_path_list:
			if is_sql_file(file_path) == True:
				file_string = file_open(file_path)
				if check_search_sting_in_file_sting(search_string,file_string) == True:		
					print(file_path)
	
	# count search result for substring in sql files
	def search_results_count(search_string, files_path_list):
		result_count = 0
		for file_path in files_path_list:
			if is_sql_file(file_path) == True:
				file_string = file_open(file_path)
				if check_search_sting_in_file_sting(search_string,file_string) == True:
					result_count += 1
		return result_count
	
	# search result list for substring in sql files
	def search_results_list(search_string, files_path_list):
		result_list = []
		for file_path in files_path_list:
			if is_sql_file(file_path) == True:
				file_string = file_open(file_path)
				if check_search_sting_in_file_sting(search_string,file_string) == True:
					result_list.append(file_path)
		return result_list
	
	search_list = all_files_paths()
	
	while True:
		search_string = input('Введите строку для поиска:\n')
		search_results_print(search_string, search_list)
		print('Всего: ', search_results_count(search_string, search_list))
		search_list = search_results_list(search_string, search_list)
		
	#pass