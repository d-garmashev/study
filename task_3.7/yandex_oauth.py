# d-garmashev_github
# https://d-garmashev.github.io/
#
# счетчик посещений https://d-garmashev.github.io/
#
# Права:
# Создание счётчиков, изменение параметров своих и доверенных счётчиков
# Получение статистики, чтение параметров своих и доверенных счётчиков
# ID: ca13fb3cc7b9477c8ca65bb31ea33c41
# Callback URL: https://oauth.yandex.ru/verification_code

# https://oauth.yandex.ru/authorize?response_type=code&client_id=ca13fb3cc7b9477c8ca65bb31ea33c41
#
# https://oauth.yandex.ru/token?grant_type=authorization_code&code=1306068&client_id=ca13fb3cc7b9477c8ca65bb31ea33c41&client_secret=01ddeab8995647f3970b714befcf0519

import requests
import base64

s = requests.Session()
s.headers['Content-type'] = 'application/x-www-form-urlencoded'
s.headers['Content-Length'] = '100'
#s.headers['Authorization'] = 'Basic ' + base64.b64encode(bytes('ca13fb3cc7b9477c8ca65bb31ea33c41:01ddeab8995647f3970b714befcf0519','utf-8')).decode("utf-8")
params = {
    'grant_type': 'authorization_code',
    'code': '4318205',
    'client_id': 'ca13fb3cc7b9477c8ca65bb31ea33c41',
    'client_secret': '01ddeab8995647f3970b714befcf0519'
}

r = s.post('https://oauth.yandex.ru/token', data=params)
print(r)
print(r.text)

# {"token_type": "bearer", "access_token": "AQAAAAAATmsfAASa6ACvwzreQUxBs73AuQpk-yY", "expires_in": 31536000, "refresh_token": "1:xrbsuqRXVg266tyd:dcy-XTM3SUhxiJ2YU2vLIhzogORaaZcYMMOk37C_swzy-y_Iwc3e:PYMZY6rO5-DGWilM6-CZSA"}
