from secrets import TOKEN
import requests
import json
from time import sleep
import datetime


def print_struct(struct):
    print(json.dumps(struct, ensure_ascii=False, indent=4))


def get_currency_rate_from_resp_data(data, currency):
    for rate in data['exchangeRate']:
        if rate.get('currency') == currency:
            return rate['saleRateNB']


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
            raise Exception(f"Пришла ошибка с апи телеги: {data}")
        return data['result']

    def send_message(self, chat_id, text):
        requests.get(self._url + '/sendMessage', {'chat_id': chat_id, 'text': text})

    def answer_to_message(self, message):
        chat_id = message['chat']['id']
        text = message['text']

        if 'привет' in text.lower() or 'hello' in text.lower() or text =='/start':
            self.send_message(chat_id, 'Вас приветствует валютный бот. Пишите курс <валюта>.\n'
                                       'Доступные валюты: USD, EUR, RUB, ...')
        elif text.startswith('курс'):
            url = 'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'
            currency = text.split(' ')[-1].strip()
            today = datetime.date.today()
            resp = requests.get(url.format(date=f"{today.day}.{today.month}.{today.year}"))
            price = get_currency_rate_from_resp_data(resp.json(), currency)
            self.send_message(chat_id, f'Курс валюты {currency} = {price}')
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
# print_struct(bot.get_updates())
# bot.send_message('358463252', 'Hi')
bot.run()
