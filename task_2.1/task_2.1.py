"""
Домашнее задание к лекции 2.1 «Открытие и чтение файла, запись в файл»

Задача №1

Воспроизведите код с лекции 1.5 и дополните его следующим образом:

Список рецептов должен храниться в отдельном файле в следующем формате:
      Название блюда
      Kоличество ингредиентов
      Название ингредиента | Количество | Единица измерения
Пример:
      Омлет
      3
      Яйца | 2 | шт
      Молоко | 50 | г
      Помидор | 100 | мл
В одном файле может быть произвольное количество блюд.
Читать список рецептов из этого файла.
Соблюдайте кодстайл, разбивайте новую логику на функции и не используйте глобальных переменных.
Код выглядел следующим образом:
"""

cook_book = {
    'яйчница': [
        {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
        {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
    ],
    'стейк': [
        {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
        {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
        {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
    ],
    'салат': [
        {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
        {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
        {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
        {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
    ]
}

def write_cook_book_to_file(filename, cook_book_dict):
    f = open(filename, "w")
    for dish in cook_book_dict.keys():
        f.write(dish)
        f.write('\n')
        f.write(str(len(cook_book_dict[dish])))
        f.write('\n')
        for ingridient in cook_book_dict[dish]:
            ingridient_string = ' '.join([ingridient['ingridient_name'], '|', str(ingridient['quantity']),
                                          '|', ingridient['measure']])
            f.write(ingridient_string)
            f.write('\n')
    f.close()

write_cook_book_to_file('cook_book.txt', cook_book)

def read_cook_book_from_file(filename):
    cook_book_from_file = {}
    with open('cook_book.txt', "r") as f:
        for line in f:
            ln = line.split('\n')[0]
            if ln.isalpha():
                dish = ln
                ingridient_list = []
            if not ln.isalpha() and not ln.isdigit():
                ingridient_dict = {'ingridient_name': ln.split(' | ')[0], 'quantity': int(ln.split(' | ')[1]),
                                   'measure': ln.split(' | ')[2]}
                ingridient_list.append(ingridient_dict)
            cook_book_from_file[dish] = ingridient_list
    f.close()
    return cook_book_from_file


cook_book_from_file = read_cook_book_from_file('cook_book.txt')

if cook_book == cook_book_from_file:
    print('OK. Cook book is saved and read correctly.')
else:
    print('Not OK')

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book_from_file[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] +=\
                    new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()