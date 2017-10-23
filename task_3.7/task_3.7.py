"""
Домашнее задание к лекции 3.7 «Работа с классами на примере API Yandex Метрика»

Создайте страничку с помощью GitHub Pages.
Установите счётчик.
Реализуйте класс доступа к API Яндекс.Метрика, который принимает токен
и предоставляет информацию о визитах, просмотрах и посетителях.
"""

import requests
from pprint import pprint
from urllib.parse import urljoin

TOKEN = 'AQAAAAAATmsfAASa6ACvwzreQUxBs73AuQpk-yY'

class YMManagementAnalytics:
    management_URL = 'https://api-metrika.yandex.ru/management/v1/'
    analytics_URL = 'https://api-metrika.yandex.ru/stat/v1/data'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        headers = {
            'Authorization': 'OAuth {}'.format(self.token),
            'Content-Type': 'appliaction/x-yametrika+json'
        }
        return headers

    def get_counters(self):
        url = urljoin(self.management_URL, 'counters')
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        return response.json()

    def print_counters(self):
        url = urljoin(self.management_URL, 'counters')
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        for counter in response.json()['counters']:
            print(counter['id'], counter['name'])

    def get_visits(self, counter_id=None):  # можно задать id счетчика, иначе берется первый по списку
        if counter_id is None:
            counter_id = self.get_counters()['counters'][0]['id']
        headers = self.get_headers()
        params = {
            'id': counter_id,
            'metrics': 'ym:s:visits',
        }
        response = requests.get(self.analytics_URL, params=params, headers=headers)
        return response.json()

    def get_pageviews(self, counter_id=None):  # можно задать id счетчика, иначе берется первый по списку
        if counter_id is None:
            counter_id = self.get_counters()['counters'][0]['id']
        headers = self.get_headers()
        params = {
            'id': counter_id,
            'metrics': 'ym:s:pageviews',
        }
        response = requests.get(self.analytics_URL, params=params, headers=headers)
        return response.json()

    def get_users(self, counter_id=None):  # можно задать id счетчика, иначе берется первый по списку
        if counter_id is None:
            counter_id = self.get_counters()['counters'][0]['id']
        headers = self.get_headers()
        params = {
            'id': counter_id,
            'metrics': 'ym:s:users',
        }
        response = requests.get(self.analytics_URL, params=params, headers=headers)
        return response.json()

my_github_counter = YMManagementAnalytics(TOKEN)
my_github_counter.print_counters()

pprint(my_github_counter.get_visits())
pprint(my_github_counter.get_pageviews())
pprint(my_github_counter.get_users())

