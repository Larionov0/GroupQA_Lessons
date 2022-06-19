import sqlite3
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('')


def get_cc():
    connection = sqlite3.connect('new.db')
    cursor = connection.cursor()
    return connection, cursor


def conn_cursor_handler_decorator(func):
    def new_func(*args, **kwargs):
        conn, cursor = get_cc()
        return func(*args, **kwargs, conn=conn, cursor=cursor)
    return new_func


def insert_in_shoes():
    id = input('Введите id: ')
    description = input('Описание обуви: ')
    measurements = input('Описание размеров: ')
    sale = input('Распродажная цена: ')
    wholesale = int(input('Оптовая цена: '))
    retail = int(input('Розничная цена: '))
    sizes = {}
    for size in range(35, 42):
        add_size = input(f'Количество {size} размера: ')
        if add_size.isdigit() and 0 < int(add_size) < 20:
            sizes[size] = int(add_size)
    return id, description, measurements, sale, wholesale, retail, sizes


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'change_db':
        change_db(callback)
    elif callback.data == 'add_in_db':
        add_in_db(callback)
    elif callback.data == 'set_id':
        mess = bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Введите id')
        bot.register_next_step_handler(mess, set_id)


@bot.message_handler(commands=['start'])
def start(message):
    main_menu(message)


def main_menu(message):
    kb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('Внести изменения в БД', callback_data='change_db')
    kb.add(btn1)
    bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb)


def change_db(callback):
    kb = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton('Добавить позицию', callback_data='add_in_db')
    btn2 = InlineKeyboardButton('Удалить позицию', callback_data='del_in_db')
    btn3 = InlineKeyboardButton('Изменить позицию', callback_data='change_in_db')
    kb.add(btn1, btn2, btn3)
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='DB Shoes',
                          reply_markup=kb)


def add_in_db(callback):
    print(callback)
    edit_menu(callback.message.chat.id, callback.message.id)


def edit_menu(chat_id, message_id):
    kb = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton('id', callback_data='set_id')
    btn2 = InlineKeyboardButton('Опсание обуви', callback_data='set_description')
    btn3 = InlineKeyboardButton('Описание размеров', callback_data='set_measurements')
    btn4 = InlineKeyboardButton('Распродажная цена', callback_data='set_sale')
    btn5 = InlineKeyboardButton('Оптовая цена', callback_data='set_wholesale')
    btn6 = InlineKeyboardButton('Розничная цена', callback_data='set_retail')
    btn7 = InlineKeyboardButton('Размеры обуви', callback_data='set_sizes')
    kb.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Добавление позиции',
                          reply_markup=kb)


@conn_cursor_handler_decorator
def set_id(message, conn, cursor):
    print(message.text)
    text = f'INSERT INTO Shoes(id) VALUES({message.text})'
    cursor.execute(text)
    conn.commit()
    edit_menu()


bot.polling()
