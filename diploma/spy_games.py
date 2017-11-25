import requests
from time import sleep

VERSION = 5.69


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

def group_name_by_id(group_id, VERSION):
    params = {'group_ids': group_id, 'v': VERSION}
    response = requests.get('https://api.vk.com/method/groups.getById', params)
    data = response.json()
    try:
        result = data['response'][0]['name']
    except:
        result = data['error']['error_msg']
    return result

# vkontakte id and token input and validation
while True:
    vkid = input('Enter vkontakte id:\n')
    TOKEN = input('Enter access token:\n')
    error_message = vk_get_groups(vkid, TOKEN, VERSION)[1]
    if len(error_message) != 0:
        print(error_message, '\n', 'Try once again')
    else:
        print('Vkontakte id and token are valid.')
        break

# list of group of given user
user_groups_list = vk_get_groups(vkid, TOKEN, VERSION)[0]

# list of friends of given user
friends_list = vk_get_friends_list(vkid, VERSION)

# dict: KEY friend(key), VALUE [groups list, error]
friends_groups_dict = get_all_friends_groups_dict(friends_list, TOKEN, VERSION)

# combined list of all group of friends
friends_groups_set = get_all_friends_groups_set(friends_groups_dict)

# set of user's groups with exclusion of all friends' groups
final_result = list(set(user_groups_list) - friends_groups_set)

# printing of task solution
print('Out of all', len(user_groups_list), 'groups of user', vkid, '-',
      len(final_result), 'groups are without friends:')

for vk_group in final_result:
    print(vk_group, group_name_by_id(vk_group, VERSION))

