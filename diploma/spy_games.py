import requests
import json
from time import sleep
from pprint import pprint
import parameters

VERSION = parameters.VERSION
TOKEN = parameters.TOKEN
VK_ID = parameters.VK_ID

ERROR_INVALID_USER_ID = 5  # vk api error code number if user doesn't exist 'Invalid user id'
ERROR_MANY_REQUESTS = 6  # vk api error code number for 'Too many requests per second'

URL_USERS_GET = 'https://api.vk.com/method/users.get'
URL_FRIENDS_GET = 'https://api.vk.com/method/friends.get'
URL_GROUPS_GET = 'https://api.vk.com/method/groups.get'

DELAY_AFTER_MANY_REQUESTS = 0.5  # the delay after "too many request" error


def call_vk_api(url, params):
    request_params = {
        'v': VERSION,
        'access_token': TOKEN
    }
    request_params.update(params)
    while True:
        response = requests.get(url, request_params)
        data = response.json()
        try:
            result = data['response']
        except (KeyError, ValueError):
            result = data['error']['error_code']
        if result == ERROR_MANY_REQUESTS:
            print('Too many requests per second. Sleep for', DELAY_AFTER_MANY_REQUESTS, 'seconds.')
            sleep(DELAY_AFTER_MANY_REQUESTS)
        else:
            break
    return result


def get_user_id_by_user_ids(user_ids):
    params = {
        'user_ids': user_ids
    }
    api_response = call_vk_api(URL_USERS_GET, params)
    try:
        result = api_response[0]['id']
    except TypeError:
        result = api_response
    return result


def vk_id_token_validation(vk_id):
    if get_user_id_by_user_ids(vk_id) != ERROR_INVALID_USER_ID:
        user_id = get_user_id_by_user_ids(vk_id)
        groups = vk_get_groups(user_id)
        if type(groups) == list:
            print('Vkontakte id and token are valid.')
        else:
            print('Error #', groups, '\n', 'Try once again.')
    else:
        print('No vk user with this id.\n Try once again.')


def vk_get_groups(vk_id):
    params = {
        'user_id': vk_id,
        'extended': 1,
        'fields': 'members_count'
    }
    api_response = call_vk_api(URL_GROUPS_GET, params)
    try:
        result = api_response['items']
    except TypeError:
        result = []
    return result


def vk_get_friends_list(vk_id):
    params = {
        'user_id': vk_id
    }
    api_response = call_vk_api(URL_FRIENDS_GET, params)
    try:
        result = api_response['items']
    except TypeError:
        result = api_response
    return result


def get_all_friends_groups_dict(friends_list):
    friends_groups_dict = {}
    for friend_index, friend in enumerate(friends_list):
        groups_list = vk_get_groups(friend)
        friends_groups_dict[friend] = groups_list
        print(" - ", friend_index + 1, "of", len(friends_list), "friends.")
    print("That's all\n")
    return friends_groups_dict


def groups_to_list(groups_dict):
    l = []
    for group in groups_dict:
        l.append(group['id'])
    return l


def get_all_friends_groups_set(friends_groups_dict):
    s = set([])
    for friend, groups in friends_groups_dict.items():
        for group in groups:
            s |= {group['id']}
    return s


def final_result_json(groups_list, final_groups_list):
    result_list = []
    for group in groups_list:
        if group['id'] in final_groups_list:
            i = {
                'name': group['name'],
                'gid': group['id'],
                'members_count': group['members_count']
            }
            result_list.append(i)
    result_dict = {'result': result_list}
    return result_dict


def json_to_file(data_dict, filename):
    with open(filename + '.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(data_dict, ensure_ascii=False))


def main():
    # vkontakte id and token input and validation
    vk_id_token_validation(VK_ID)

    # convert text or numeric vk_id to numeric
    user_id = get_user_id_by_user_ids(VK_ID)

    # list of group of given user
    user_groups_list = vk_get_groups(user_id)

    # list of friends of given user
    # friends_list = vk_get_friends_list(user_id)[:10]
    friends_list = vk_get_friends_list(user_id)

    # dict: KEY friend(key), VALUE [groups list, error]
    friends_groups_dict = get_all_friends_groups_dict(friends_list)

    # combined list of all group of friends
    friends_groups_set = get_all_friends_groups_set(friends_groups_dict)

    # set of user's groups with exclusion of all friends' groups
    final_groups_list = list(set(groups_to_list(user_groups_list)) - friends_groups_set)

    # printing of task solution
    print('Out of all', len(user_groups_list), 'groups of user', user_id, '-',
          len(final_groups_list), 'groups are without friends:')

    final_result_dict = final_result_json(user_groups_list, final_groups_list)
    pprint(final_result_dict)
    json_to_file(final_result_dict, 'final_result_v3')


main()
