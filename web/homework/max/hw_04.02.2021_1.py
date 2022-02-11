import requests
import json
import datetime
import plotly.graph_objs as go


def print_json(dct):
    print(json.dumps(dct, indent=4))


def get_currency_rate_from_resp_data(data, currency):
    for rate in data["exchangeRate"]:
        if rate.get("currency") == currency:
            return rate["saleRateNB"]


def draw_currency_diagram(years, prices, currency):
    diag = go.Scatter(x=years, y=prices)
    go.Figure(data=[diag]).write_html(f"{currency}_rates.html", auto_open=True)


def draw_diagram_by_currency_rate_for_year(url, currency="EUR", year=2015):
    url = url

    months = []
    prices = []
    for month in range(1, 13):
        month_for_resp = month if month >= 10 else f'0{month}'
        print(f"Собираем данные за {month_for_resp}.{year}")
        resp = requests.get(url.format(date=f"01.{month_for_resp}.{year}"))
        price = get_currency_rate_from_resp_data(resp.json(), currency)
        prices.append(price)
        months.append(month)
    draw_currency_diagram(months, prices, currency)


url = "https://api.privatbank.ua/p24api/exchange_rates?json&date={date}"

while True:
    print("\n--MENU--\n"
          "1. Ввести дату и валюту\n"
          "2. Ввести год и валюту\n")
    choice = input()

    if choice == '1':
        date = input('Введите дату "01.02.2018": ')
        currency = input("Введите валюту: ")
        resp = requests.get(url.format(date=f"{date}"))
        print(get_currency_rate_from_resp_data(resp.json(), currency='EUR'))

    elif choice == '2':
        year = input('Введите год: ')
        currency = input("Введите валюту: ")
        draw_diagram_by_currency_rate_for_year(url, currency, year)

    else:
        break