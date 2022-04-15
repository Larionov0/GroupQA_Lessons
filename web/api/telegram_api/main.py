from secrets import TOKEN
import requests
import json
from time import sleep
import datetime

from typing import Dict


def print_struct(struct):
    print(json.dumps(struct, ensure_ascii=False, indent=4))


class User:
    def __init__(self, chat_id, username, coins=0):
        self.chat_id = chat_id
        self.username = username
        self.coins = coins
        self.phone_number = None
        self.next_message_handler = None

    @classmethod
    def create_default_user(cls, chat_id):
        return cls(chat_id, 'new_user')

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return self.__str__()


class Bot:
    BASE_URL = f'https://api.telegram.org/bot'

    def __init__(self, token=TOKEN):
        self._token = token
        self._url = self.BASE_URL + token
        self._last_update_id = 0
        self._users: Dict[int, User] = {}

    def get_updates(self):
        resp = requests.get(self._url + '/getUpdates', {'offset': self._last_update_id + 1})
        data = resp.json()
        if not data['ok']:
            raise Exception(f"Пришла ошибка с апи телеги: {data}")
        return data['result']

    def send_message_to_user(self, user, text):
        self.send_message(user.chat_id, text)

    def send_message(self, chat_id, text):
        requests.get(self._url + '/sendMessage', {'chat_id': chat_id, 'text': text})

    def _full_answer_to_to_message(self, message):
        chat_id = message['chat']['id']
        text = message['text']

        user = self._get_user_by_chat_id(chat_id)
        self._answer_to_message(user, text)

    def _get_user_by_chat_id(self, chat_id):
        if chat_id in self._users:
            return self._users[chat_id]
        else:  # у нас новый юзер
            return self._create_new_user(chat_id)

    def _create_new_user(self, chat_id):
        user = User.create_default_user(chat_id)
        self._users[chat_id] = user
        return user

    def run(self):
        while True:
            updates = self.get_updates()
            for update in updates:
                if 'message' in update:
                    self._full_answer_to_to_message(update['message'])
                self._last_update_id = update['update_id']
            sleep(0.5)

    def _answer_to_message(self, user: User, text: str):
        if user.next_message_handler:
            user.next_message_handler(user, text)
        else:
            self.main_menu(user)

    def main_menu(self, user):
        text = f'--= Главное меню =--\n' \
               f'Пользователь {user.username}\n' \
               f'1 - магазин\n' \
               f'2 - настройки аккаунта\n' \
               f'3 - регламент\n'
        self.send_message_to_user(user, text)
        user.next_message_handler = self.main_menu_handler

    def main_menu_handler(self, user, text):
        if text == '1':
            pass
        elif text == '2':
            self.account_settings_menu(user)
        elif text == '3':
            self.send_message_to_user(user, '*документы*')

    def account_settings_menu(self, user):
        text = f'--= Аккаунт =--\n' \
               f'никнейм: {user.username}\n' \
               f'телефон: {user.phone_number}\n' \
               f'монеты: {user.coins}\n' \
               f'1 - сменить никнейм\n' \
               f'2 - сменить телефон\n' \
               f'3 - назад'
        self.send_message_to_user(user, text)
        user.next_message_handler = self.account_settings_menu_handler

    def account_settings_menu_handler(self, user, text):
        if text == '1':
            self.change_username_menu(user)
        elif text == '2':
            pass
        elif text == '3':
            self.main_menu(user)

    def change_username_menu(self, user):
        self.send_message_to_user(user, 'Введите новый никнейм:')
        user.next_message_handler = self.change_username_menu_handler

    def change_username_menu_handler(self, user, text):
        if 5 <= len(text) <= 20:
            user.username = text
            self.send_message_to_user(user, 'Юзернейм сохранен!')
            self.account_settings_menu(user)
        else:
            self.send_message_to_user(user, 'Длина должна быть от 5 до 20 символов')
            self.change_username_menu(user)


bot = Bot()
# print_struct(bot.get_updates())
# bot.send_message('358463252', 'Hi')
bot.run()
# bot.send_message(358463252, 'Hi from Python')
