from secrets import TOKEN
import requests
import json
from time import sleep
import datetime


def print_struct(struct):
    print(json.dumps(struct, ensure_ascii=False, indent=4))


def ingredients_in_cocktail(cocktail):
    url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={cocktail}'
    response = requests.get(url).json()
    # print_struct(response)
    ingredients = response['drinks'][0]
    text = ''
    for el in ingredients:
        if 'strIngredient' in el and ingredients[el] is not None:
            text += f"{ingredients[el]}\n"
    text += '\n' + ingredients['strDrinkThumb']
    return text


def get_currency_rate_from_resp_data(data, currency):
    for rate in data["exchangeRate"]:
        if rate.get("currency") == currency:
            return rate["saleRateNB"]


def currency_rate_for_year(currency="EUR", year=2015):
    url = "https://api.privatbank.ua/p24api/exchange_rates?json&date={date}"

    months = []
    prices = []
    for month in range(1, 13):
        month_for_resp = month if month >= 10 else f'0{month}'
        resp = requests.get(url.format(date=f"01.{month_for_resp}.{year}"))
        price = get_currency_rate_from_resp_data(resp.json(), currency)
        prices.append(price)
        months.append(month)
    return ''.join([f'{el[0]} - {el[1]} {currency}\n' for el in list(zip(months, prices))])


class Bot:
    BASE_URL = f'https://api.telegram.org/bot'

    def __init__(self, token=TOKEN):
        self._token = token
        self._url = self.BASE_URL + token
        self._last_update_id = 0

    def get_updates(self):
        resp = requests.get(self._url + '/getUpdates', {'offset': self._last_update_id + 1})
        data = resp.json()
        if not data['ok']:
            raise Exception(f'Return error: {data}')
        return data['result']

    def send_message(self, chat_id, text):
        requests.get(self._url + f'/sendMessage', {'chat_id': chat_id, 'text': text})

    def answer_to_message(self, message):
        chat_id = message['chat']['id']
        text = message['text']
        text_lst = text.split()

        if 'привет' in text.lower() or 'hello' in text.lower() or text == '/start':
            self.send_message(chat_id, 'Калькулятор, пример: (2 + 2)\n'
                                       'Список курсов, пример: курс EUR 2019\n'
                                       'Состав коктейлей, пример: коктейль(или cocktail) <sex on the bitch>')

        elif text_lst[0].isdigit() and len(text_lst) >= 3 and text_lst[-1].isdigit() and text_lst[1] in '/*-+':  # 2+4
            try:
                self.send_message(chat_id, eval(text))
            except Exception as ex:
                print(f"Ошибка: {ex}")
                self.send_message(chat_id, 'Неправильный формат введения!')

        elif text_lst[0].lower() == 'курс':
            try:
                self.send_message(chat_id, 'Собираем данные...')
                rate = currency_rate_for_year(text_lst[1], text_lst[2])
                self.send_message(chat_id, rate)
            except Exception as ex:
                self.send_message(chat_id, f"Ошибка: {ex}")

        elif text_lst[0].lower() == 'коктейль' or text_lst[0].lower() == 'cocktail':
            try:
                ingredients = ingredients_in_cocktail(text_lst[1])
                self.send_message(chat_id, f'Состав:\n{ingredients}')
            except Exception as ex:
                self.send_message(chat_id, f"Ошибка: {ex}")

        else:
            self.send_message(chat_id, text + ')')

    def run(self):
        while True:
            updates = self.get_updates()
            for update in updates:
                if 'message' in update:
                    self.answer_to_message(update['message'])
                self._last_update_id = update['update_id']
            sleep(0.5)


bot = Bot()
bot.run()
