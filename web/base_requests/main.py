import requests


response = requests.get('https://rozetka.com.ua/notebooks/c80004/')

with open('test_file.html', 'wt', encoding='utf-8') as file:
    file.write(response.text)
