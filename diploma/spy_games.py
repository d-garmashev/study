import requests
import json
import codecs
from time import sleep
from pprint import pprint

VERSION = 5.69


def get_user_id_by_user_ids(user_ids, VERSION):
    params = {
        'user_ids': user_ids,
        'v': VERSION
    }
    response = requests.get('https://api.vk.com/method/users.get', params)
    data = response.json()
    try:
        result = data['response'][0]['id']
    except:
        result = data['error']['error_msg']
    sleep(0.33)
    return result


def vk_get_groups(vkid, TOKEN, VERSION):
    params = {
        'user_id': vkid,
        'access_token': TOKEN,
        'v': VERSION
    }
    response = requests.get('https://api.vk.com/method/groups.get', params)
    data = response.json()
    result = []
    error = ''
    try:
        result = data['response']['items']
    except:
        error = data['error']['error_msg']
        if error == 'Too many requests per second':
            sleep(3)
            response = requests.get('https://api.vk.com/method/groups.get', params)
            data = response.json()
            try:
                result = data['response']['items']
            except:
                result = []
                error = data['error']['error_msg']
    sleep(0.33)
    return [result, error]


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


def get_all_friends_groups_dict(friends_list, TOKEN, VERSION):
    friends_groups_dict = {}
    i = 1
    for friend in friends_list:
        groups_list = vk_get_groups(friend, TOKEN, VERSION)
        friends_groups_dict[friend] = groups_list
        print(" - ", i, "of", len(friends_list), "friends.")
        i += 1
    print("That's all\n")
    return friends_groups_dict


def get_all_friends_groups_set(friends_groups_dict):
    s = set([])
    for friend in friends_groups_dict:
        s = s | set(friends_groups_dict[friend][0])
    return s


def group_members_count(group_id, VERSION):
    params = {
        'group_id': group_id,
        'access_token': TOKEN,
        'v': VERSION
    }
    response = requests.get('https://api.vk.com/method/groups.getMembers', params)
    data = response.json()
    try:
        result = data['response']['count']
    except:
        result = data['error']['error_msg']
    sleep(0.33)
    return result


def group_name_by_id(group_id, VERSION):
    params = {'group_ids': group_id, 'v': VERSION}
    response = requests.get('https://api.vk.com/method/groups.getById', params)
    data = response.json()
    try:
        result = data['response'][0]['name']
    except:
        result = data['error']['error_msg']
    sleep(0.33)
    return result


def final_result_json(groups_list, VERSION):
    result_list = []
    for group in groups_list:
        i = {
            'name': group_name_by_id(group, VERSION),
            'gid': group,
            'members_count': group_members_count(group, VERSION)
        }
        print(" - ")
        result_list.append(i)
    result_dict = {}
    result_dict['result'] = result_list
    return result_dict


def json_to_file(data_dict, filename):
    with codecs.open(filename + '.json', 'w', 'utf8') as f:
        f.write(json.dumps(data_dict, ensure_ascii=False))


# vkontakte id and token input and validation
while True:
    user_id = input('Enter vkontakte id:\n')
    if get_user_id_by_user_ids(user_id, VERSION) != 'Invalid user id':
        vkid = get_user_id_by_user_ids(user_id, VERSION)
        TOKEN = input('Enter access token:\n')
        error_message = vk_get_groups(vkid, TOKEN, VERSION)[1]
        if len(error_message) != 0:
            print(error_message, '\n', 'Try once again.')
        else:
            print('Vkontakte id and token are valid.')
            break
    else:
        print('No vk user with this id.\n Try once again.')


# list of group of given user
user_groups_list = vk_get_groups(vkid, TOKEN, VERSION)[0]

# list of friends of given user
friends_list = vk_get_friends_list(vkid, VERSION)

# dict: KEY friend(key), VALUE [groups list, error]
friends_groups_dict = get_all_friends_groups_dict(friends_list, TOKEN, VERSION)

# combined list of all group of friends
friends_groups_set = get_all_friends_groups_set(friends_groups_dict)

# set of user's groups with exclusion of all friends' groups
final_groups_list = list(set(user_groups_list) - friends_groups_set)

# printing of task solution
print('Out of all', len(user_groups_list), 'groups of user', vkid, '-',
      len(final_groups_list), 'groups are without friends:')

# printing and saving final results
final_result_dict = final_result_json(final_groups_list, VERSION)
pprint(final_result_dict)
json_to_file(final_result_dict, 'final_result')
