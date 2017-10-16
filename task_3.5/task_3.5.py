import osa
import math

"""
Задача №1

Дано: семь значений температур по Фаренгейту в файле temps.txt.
Необходимо вывести среднюю за неделю арифметическую температуру по Цельсию.

"""

def temps_file_to_list(file_path):
    with open(file_path) as f:
        content = f.read().split(' F')
    content = content[:-1]
    content = [int(x.strip()) for x in content]
    return(content)

def farenheit_to_celsius(fr_temperature):
    URL1 = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
    client1 = osa.client.Client(URL1)
    response1 = client1.service.ConvertTemp(Temperature=fr_temperature, FromUnit='degreeFahrenheit', ToUnit='degreeCelsius')
    return(response1)

def list_avg(list):
    avg_list = sum(fr_temps_list) / float(len(fr_temps_list))
    return(avg_list)

file_path_temps = 'Homework\\temps.txt'

fr_temps_list = temps_file_to_list(file_path_temps)
avg_week_fr_temperature = list_avg(fr_temps_list)
avg_week_cs_temperature = round(farenheit_to_celsius(avg_week_fr_temperature), 2)
print("Task 1:", avg_week_cs_temperature)

"""
Задача №2

Вы собираетесь отправиться в путешествие и начинаете разрабатывать маршрут 
и выписывать цены на перелеты. Даны цены на билеты в местных валютах 
(файл currencies.txt). Формат данных в файле:

<откуда куда>: <стоимость билета> <код валюты>
Пример:
MOSCOW-LONDON: 120 EUR
Посчитайте, сколько вы потратите на путешествие денег в рублях (без копеек, округлить в большую сторону).

"""


def cur_file_to_list_of_lists(cur_file_path):
    with open(cur_file_path) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = [x.split(' ') for x in content]
    return(content)

def convert_to_rub(from_cur, amount_in_cur):
    URL4 = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
    client4 = osa.client.Client(URL4)
    response4 = client4.service.ConvertToNum(toCurrency='RUB', fromCurrency=from_cur,
                                             amount=amount_in_cur, rounding=True)
    return(response4)

def prices_rub(data_cur):
    result_rub = []
    for route in data_cur:
        result_rub.append(convert_to_rub(route[2], route[1]))
    return(result_rub)


cur_file_path = 'Homework\\currencies.txt'
data_cur = cur_file_to_list_of_lists(cur_file_path)
result_sum = sum(prices_rub(data_cur))
result_sum_round_up = math.ceil(result_sum)
print("Task 2:", result_sum_round_up)

"""
Задача №3

Дано: длина пути в милях, название пути (файл travel.txt) в формате:

<название пути>: <длина в пути> <мера расстояния>
Пример:
MOSCOW-LONDON: 1,553.86 mi
Необходимо посчитать суммарное расстояние пути в километрах с точностью до сотых.

"""


def travel_file_to_list(travel_file_path):
    with open(travel_file_path) as f:
        content = f.readlines()
    content = [x.replace(',', '') for x in content]
    content = [x.strip() for x in content]
    content = [x.split(' ') for x in content]
    content = [float(x[1]) for x in content]
    return(content)

def miles_to_km(miles_value):
    URL5 = 'http://www.webservicex.net/length.asmx?WSDL'
    client5 = osa.client.Client(URL5)
    response5 = client5.service.ChangeLengthUnit(fromLengthUnit='Miles', toLengthUnit='Kilometers',
                                                 LengthValue=miles_value)
    return(response5)


travel_file_path = 'Homework\\travel.txt'

list_distance_in_miles = travel_file_to_list(travel_file_path)
sum_distance_in_miles = round(sum(list_distance_in_miles), 2)
print("Task 3:", sum_distance_in_miles)

