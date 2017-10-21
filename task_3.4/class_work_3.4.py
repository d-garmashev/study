from urllib.parse import urlencode
import requests
from pprint import pprint

AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
APP_ID = 5237973
VERSION = 5.68

# params = {
#     'client_id': APP_ID,
#     'display': 'page',
#     'redirect_uri': 'https://oauth.vk.com/blank.html',
#     'scope': 'friends,status',
#     'response_type': 'token',
#     'v': VERSION
# }

# print('?'.join(
#     (AUTHORIZE_URL, urlencode(params))
# ))


TOKEN = 'f3f157f19b1939d09a15d545a3dad0eca05dbe481fa962062638d705f4e83819df0cee827b74970d2b332'

params = {
    'v': VERSION,
    'access_token': TOKEN
}

response = requests.get('https://api.vk.com/method/status.get', params)

data = response.json()
pprint(data)