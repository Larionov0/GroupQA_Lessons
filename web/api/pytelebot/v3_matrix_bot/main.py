import telebot
from misc import TOKEN
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


# Можем использовать эти переменные как глобальные
bot = telebot.TeleBot(TOKEN)
users = []


class User:
    def __init__(self, chat_id, username='new user', gold=0):
        self.chat_id = chat_id
        self.username = username
        self.gold = gold
        self.message_id = None  # последнее сообщение от бота юзеру
        self._help_message = ''  # для доп информации в текущей меню (любой, где это нужно)

    def clear_help_message(self):
        self._help_message = ''

    @property
    def help_message(self):
        msg = self._help_message
        self.clear_help_message()
        return msg

    @help_message.setter
    def help_message(self, text):  # obj.help_message = 'afsdgf'
        self._help_message = text

    def try_to_save_my_message(self, message):
        if self.message_id is None:
            self.message_id = message.message_id

    def delete_last_message(self):
        if self.message_id:
            bot.delete_message(self.chat_id, self.message_id)

    def delete_my_message(self, message):
        bot.delete_message(self.chat_id, message.message_id)

    def resend_message(self, text, reply_markup=None):
        self.delete_last_message()
        message = bot.send_message(self.chat_id, text, reply_markup=reply_markup)
        self.message_id = message.message_id

    @classmethod
    def create_user(cls, chat_id):
        user = User(chat_id)
        users.append(user)
        return user

    @classmethod
    def find_user(cls, chat_id) -> 'User':
        for user in users:
            if user.chat_id == chat_id:
                return user

        # не нашли -> нужно создать
        user = cls.create_user(chat_id)
        return user

    @classmethod
    def find_user_from_message(cls, message):
        return cls.find_user(message.chat.id)

    @classmethod
    def find_user_and_delete_message(cls, message):
        user = cls.find_user_from_message(message)
        user.delete_my_message(message)
        return user


@bot.message_handler(content_types=['text'])
def text_handler(message):
    user = User.find_user_and_delete_message(message)
    main_menu(user)


def main_menu(user):
    text = '---= Главное меню =---'
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.row(KeyboardButton('Играть'), KeyboardButton('Магазин'))
    keyboard.row(KeyboardButton('Настройки аккаунта'))
    user.resend_message(text, keyboard)
    bot.register_next_step_handler_by_chat_id(user.chat_id, main_handler)


def main_handler(message):
    user = User.find_user_and_delete_message(message)
    text = message.text.lower()
    if 'играть' in text:
        pass
    elif 'настройки аккаунта' in text:
        account_settings_menu(user)


def account_settings_menu(user):
    text = '--= Настройки аккаунта =--\n' \
           f'Ваш никнейм: {user.username}\n' \
           f'Ваше золото: {user.gold}\n\n' \
           f'{user.help_message}'
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.row(KeyboardButton('Изменить никнейм'))
    keyboard.row(KeyboardButton('Назад'))
    user.resend_message(text, keyboard)
    bot.register_next_step_handler_by_chat_id(user.chat_id, account_settings_handler)


def account_settings_handler(message):
    user = User.find_user_and_delete_message(message)
    text = message.text.lower()
    if 'изменить никнейм' in text:
        user.resend_message('Введите новый никнейм:')
        bot.register_next_step_handler_by_chat_id(user.chat_id, new_nickname_handler)
    elif 'назад' in text:
        main_menu(user)


def new_nickname_handler(message):
    user = User.find_user_and_delete_message(message)
    new_nickname = message.text
    if 6 <= len(new_nickname) <= 20 and ' ' not in new_nickname:
        user.username = new_nickname
        user.help_message = 'Никнейм обновлен'
        account_settings_menu(user)
    else:
        user.help_message = 'Никнейм не принят'
        account_settings_menu(user)


bot.polling()
