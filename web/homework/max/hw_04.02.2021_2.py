import requests
import json
from translate import Translator


def print_json(dct):
    print(json.dumps(dct, indent=4))


def weather(text):
    translator = Translator(from_lang="russian", to_lang="english")
    city = translator.translate(text)

    key = 'c10af5c49d55a65db684841f136ec9bb'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}'

    resp = requests.get(url)
    data = resp.json()
    # print_json(data)
    return f'\nНебо: {data["weather"][0]["description"]}\nТемпература min: {data["main"]["temp_min"]}\n' \
           f'Температура max: {data["main"]["temp_max"]}'


while True:
    print('\n--ПОГОДА В ГОРОДЕ--')
    city = input('ВВедите город (рус.яз): ')

    print(weather(city))
