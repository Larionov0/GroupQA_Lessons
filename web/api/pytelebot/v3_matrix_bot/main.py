import telebot
from misc import TOKEN
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from classes.user import User
from classes.lobby import Lobby


# Можем использовать эти переменные как глобальные
bot = telebot.TeleBot(TOKEN)
Lobby.lobbies.append(Lobby('первое лобби'))
Lobby.lobbies.append(Lobby('второе лобби'))


@bot.message_handler(content_types=['text'])
def text_handler(message):
    user = User.find_user_and_delete_message(message, bot)
    main_menu(user)


@bot.callback_query_handler(lambda call: True)
def inline_button_handler(call):  # ПРИ НАЖАТИИ НА ИНЛАЙН КНОПОЧКУ
    user = User.find_user_from_message(call.message, bot)
    bot.answer_callback_query(call.id)

    if call.data == 'back':
        return main_menu(user)

    lobby = Lobby.find_lobby(call.data)
    result = lobby.enter(user)

    if result:
        for user in lobby.users:
            lobby_menu(user)
    else:
        user.resend_message('Не удалось войти, так как лобби заполнено')


def main_menu(user):
    text = '---= Главное меню =---'
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.row(KeyboardButton('Играть'), KeyboardButton('Магазин'))
    keyboard.row(KeyboardButton('Настройки аккаунта'))
    user.resend_message(text, keyboard)
    bot.register_next_step_handler_by_chat_id(user.chat_id, main_handler)


def main_handler(message):
    user = User.find_user_and_delete_message(message, bot)
    text = message.text.lower()
    if 'играть' in text:
        lobbies_menu(user)
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
    user = User.find_user_and_delete_message(message, bot)
    text = message.text.lower()
    if 'изменить никнейм' in text:
        user.resend_message('Введите новый никнейм:')
        bot.register_next_step_handler_by_chat_id(user.chat_id, new_nickname_handler)
    elif 'назад' in text:
        main_menu(user)


def new_nickname_handler(message):
    user = User.find_user_and_delete_message(message, bot)
    new_nickname = message.text
    if 6 <= len(new_nickname) <= 20 and ' ' not in new_nickname:
        user.username = new_nickname
        user.help_message = 'Никнейм обновлен'
        account_settings_menu(user)
    else:
        user.help_message = 'Никнейм не принят'
        account_settings_menu(user)


def lobbies_menu(user):
    keyboard = InlineKeyboardMarkup()
    for lobby in Lobby.lobbies:
        keyboard.row(InlineKeyboardButton(str(lobby), callback_data=lobby.name))
    keyboard.row(InlineKeyboardButton('назад', callback_data='back'))
    user.resend_message('--= Лобби =--', keyboard)


def lobby_menu(main_user):
    text = f'---= Лобби {main_user.lobby.name} =---\n'
    for user in main_user.lobby.users:
        text += f"- {user.username}\n"
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.row(KeyboardButton('выход'))
    main_user.resend_message(text, keyboard)
    bot.register_next_step_handler_by_chat_id(user.chat_id, lobby_menu_handler)


def lobby_menu_handler(message):
    user = User.find_user_and_delete_message(message, bot)
    if message.text == 'выход':
        user.exit_lobby()
        lobby_menu(user)


def test_handler(call):
    print(call)


bot.polling()
