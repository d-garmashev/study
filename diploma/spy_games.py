import requests
import json
from time import sleep
from pprint import pprint
import parameters

VERSION = parameters.VERSION
TOKEN = parameters.TOKEN
VK_ID = parameters.VK_ID

URL_USERS_GET = 'https://api.vk.com/method/users.get'
URL_FRIENDS_GET = 'https://api.vk.com/method/friends.get'
URL_GROUPS_GET = 'https://api.vk.com/method/groups.get'
URL_GROUPS_GET_BY_ID = 'https://api.vk.com/method/groups.getById'
URL_GROUPS_GET_MEMBERS = 'https://api.vk.com/method/groups.getMembers'

REQUEST_DELAY = 0.1  # vkontakte API request delay to avoid "too many request" error
DELAY_AFTER_MANY_REQUESTS = 0.3  # the delay after "too many request" error


def call_vk_api(url, params):
    response = requests.get(url, params)
    data = response.json()
    try:
        result = data['response']
    except (KeyError, ValueError):
        result = data['error']['error_code']
        if result == 6:  # 'Too many requests per second'
            print('Too many requests per second')
            sleep(DELAY_AFTER_MANY_REQUESTS)
            response = requests.get(url, params)
            data = response.json()
            try:
                result = data['response']['items']
            except (KeyError, ValueError):
                result = data['error']['error_code']
    sleep(REQUEST_DELAY)
    return result


def get_user_id_by_user_ids(user_ids, version):
    params = {
        'user_ids': user_ids,
        'v': version
    }
    api_response = call_vk_api(URL_USERS_GET, params)
    try:
        result = api_response[0]['id']
    except TypeError:
        result = api_response
    return result


def vk_id_token_validation(vk_id, token, version):
    if get_user_id_by_user_ids(vk_id, version) != 5:  # 'Invalid user id'
        user_id = get_user_id_by_user_ids(vk_id, version)
        groups = vk_get_groups(user_id, token, version)
        if type(groups) == list:
            print('Vkontakte id and token are valid.')
        else:
            print('Error #', groups, '\n', 'Try once again.')
    else:
        print('No vk user with this id.\n Try once again.')


def vk_get_groups(vk_id, token, version):
    params = {
        'user_id': vk_id,
        'access_token': token,
        'v': version
    }
    api_response = call_vk_api(URL_GROUPS_GET, params)
    try:
        result = api_response['items']
    except TypeError:
        result = []
    return result


def vk_get_friends_list(vk_id, version):
    params = {
        'user_id': vk_id,
        'v': version
    }
    api_response = call_vk_api(URL_FRIENDS_GET, params)
    try:
        result = api_response['items']
    except TypeError:
        result = api_response
    return result

def get_all_friends_groups_dict(friends_list, token, version):
    friends_groups_dict = {}
    for friend_index, friend in enumerate(friends_list):
        groups_list = vk_get_groups(friend, token, version)
        friends_groups_dict[friend] = groups_list
        print(" - ", friend_index + 1, "of", len(friends_list), "friends.")
    print("That's all\n")
    return friends_groups_dict


def get_all_friends_groups_set(friends_groups_dict):
    s = set([])
    for friend, groups in friends_groups_dict.items():
        try:
            s |= set(groups)
        except TypeError:
            s |= {groups}  # if groups not a list, but single value - user with 1 group
    return s


def group_members_count(group_id, token, version):
    params = {
        'group_id': group_id,
        'access_token': token,
        'v': version
    }
    api_response = call_vk_api(URL_GROUPS_GET_MEMBERS, params)
    try:
        result = api_response['count']
    except TypeError:
        result = 0
    return result


def group_name_by_id(group_id, version):
    params = {
        'group_ids': group_id,
        'v': version
    }
    api_response = call_vk_api(URL_GROUPS_GET_BY_ID, params)
    try:
        result = api_response[0]['name']
    except TypeError:
        result = ''
    return result


def final_result_json(groups_list, token, version):
    result_list = []
    for group in groups_list:
        i = {
            'name': group_name_by_id(group, version),
            'gid': group,
            'members_count': group_members_count(group, token, version)
        }
        print(" - ")
        result_list.append(i)
    result_dict = {'result': result_list}
    return result_dict


def json_to_file(data_dict, filename):
    with open(filename + '.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(data_dict, ensure_ascii=False))


# vkontakte id and token input and validation
vk_id_token_validation(VK_ID, TOKEN, VERSION)

# convert text or numeric vk_id to numeric
user_id = get_user_id_by_user_ids(VK_ID, VERSION)

# list of group of given user
user_groups_list = vk_get_groups(user_id, TOKEN, VERSION)

# list of friends of given user
friends_list = vk_get_friends_list(user_id, VERSION)

# dict: KEY friend(key), VALUE [groups list, error]
friends_groups_dict = get_all_friends_groups_dict(friends_list, TOKEN, VERSION)

# combined list of all group of friends
friends_groups_set = get_all_friends_groups_set(friends_groups_dict)

# set of user's groups with exclusion of all friends' groups
final_groups_list = list(set(user_groups_list) - friends_groups_set)

# printing of task solution
print('Out of all', len(user_groups_list), 'groups of user', user_id, '-',
      len(final_groups_list), 'groups are without friends:')

# printing and saving final results
final_result_dict = final_result_json(final_groups_list, TOKEN, VERSION)
pprint(final_result_dict)
json_to_file(final_result_dict, 'final_result_v2')
