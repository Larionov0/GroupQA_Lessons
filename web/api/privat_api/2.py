import requests
import json
import datetime
import plotly.graph_objs as go


def print_struct(dct):
    print(json.dumps(dct, indent=4, ensure_ascii=False))


def get_currency_rate_from_resp_data(data, currency):
    for rate in data['exchangeRate']:
        if rate.get('currency') == currency:
            return rate['saleRateNB']


def draw_currency_diagram(years, prices, currency):
    diag = go.Scatter(x=years, y=prices)
    go.Figure(data=[diag]).write_html(f'{currency}_rates.html', auto_open=True)


def draw_diagram_by_currency_rate_for_years(currency='EUR', start_year=2015, end_year=None):
    url = 'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'

    if end_year is None:
        end_year = datetime.date.today().year

    years = []
    prices = []
    for year in range(start_year, end_year + 1):
        print(f"Собираем данные за год {year}")
        resp = requests.get(url.format(date=f"01.01.{year}"))
        price = get_currency_rate_from_resp_data(resp.json(), currency)
        prices.append(price)
        years.append(year)
    draw_currency_diagram(years, prices, currency)


draw_diagram_by_currency_rate_for_years()
