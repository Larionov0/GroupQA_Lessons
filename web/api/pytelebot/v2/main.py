import telebot
from misc import TOKEN
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Приветствуем вас в нашем боте 🤩')
    main_menu(message)


def main_menu(message):
    text = '---= Главное меню =---'

    keyboard = ReplyKeyboardMarkup()
    keyboard.row(KeyboardButton('Магазин🛒'), KeyboardButton('Игра🎮'))
    keyboard.row(KeyboardButton('Документы📜'))

    bot.send_message(message.chat.id, text, reply_markup=keyboard)
    bot.register_next_step_handler_by_chat_id(message.chat.id, main_menu_handler)


def main_menu_handler(message):
    text = message.text.lower()
    if text.startswith('магазин'):
        store_menu(message)
    elif text.startswith('игра'):
        pass
    elif text.startswith('документы'):
        pass


def store_menu(message):
    text = '---= Магазин =---\n' \
           '1 - байрактар\n' \
           '2 - донат на ВСУ\n' \
           '3 - назад\n'

    keyboard = ReplyKeyboardMarkup()
    keyboard.row(KeyboardButton('байрактар'), KeyboardButton('донат на ВСУ'))
    keyboard.row(KeyboardButton('назад'))

    bot.send_message(message.chat.id, text, reply_markup=keyboard)
    bot.register_next_step_handler_by_chat_id(message.chat.id, store_menu_handler)


def store_menu_handler(message):
    text = message.text.lower()
    if text.startswith('байрактар'):
        bot.send_message(message.chat.id, 'Байрактары уже распроданы')
        store_menu(message)
    elif text.startswith('донат'):
        pass
    elif text.startswith('назад'):
        main_menu(message)


bot.polling(none_stop=True)
