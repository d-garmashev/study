# Домашнее задание к лекции 3.4 «Работа с API ВК, json, протокол OAuth»
#
# Получите список всех своих друзей;
# Для каждого своего друга получите список его друзей;
# Найдите пересечения (общих друзей) между всеми пользователями.

# для метода friends.get OAuth не нужен

import requests
from time import sleep
from collections import Counter

VERSION = 5.68
my_vkid = 499331

def vk_get_friends_list(vkid, VERSION):
    params = {
        'user_id': vkid,
        'v': VERSION
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    data = response.json()
    try:
        result = data['response']['items']
    except:
        result = data['error']['error_msg']
    return result


def friends_of_friends(my_vkid, VERSION):
    j = 1
    friends_of_friends_list = []
    my_friends_list =  vk_get_friends_list(my_vkid, VERSION)
    #for i in my_friends_list[:20]: # более короткий цикл для теста
    for i in my_friends_list:
        print(j, 'of', len(my_friends_list), 'friends checked')
        j += 1
        if type(vk_get_friends_list(i, VERSION)) is list:  # проверка на тип возвращаемых данных
            friends_of_friends_list.append(vk_get_friends_list(i, VERSION))
        elif vk_get_friends_list(i, VERSION) == 'Access denied: user deactivated':  # обработка ошибки удаленной страницы
            pass
        else:  # для ошибки более 3 запросов в секунду - повтор операции
            sleep(1)
            if type(vk_get_friends_list(i, VERSION)) is list:
                friends_of_friends_list.append(vk_get_friends_list(i, VERSION))
    print(len(friends_of_friends_list), 'friends-of-friends lists found')
    return friends_of_friends_list


def list_of_lists_to_list(list_of_lists):
    result = []
    for i in list_of_lists:
        result += i
    return result


my_friends_of_friends_list = friends_of_friends(my_vkid, VERSION)
fof_list = Counter(list_of_lists_to_list(my_friends_of_friends_list)).most_common()

if fof_list[0][0] == my_vkid and fof_list[1][1] < fof_list[0][1]:
        print("There are no common friends between my friends besides me.")
        print("My friend", fof_list[1][0], "has", fof_list[1][1], "connections out of maximum",
              len(my_friends_of_friends_list))
else:
    print('It gets suspicious. Rare case.')
