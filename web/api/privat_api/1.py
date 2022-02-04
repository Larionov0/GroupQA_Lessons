import requests
import json


def print_struct(dct):
    print(json.dumps(dct, indent=4, ensure_ascii=False))


CURRENCY = 'EUR'

date = '04.02.2022'
url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'

resp = requests.get(url)
data = resp.json()

for rate in data['exchangeRate']:
    if rate.get('currency') == CURRENCY:
        print(rate['saleRateNB'])
