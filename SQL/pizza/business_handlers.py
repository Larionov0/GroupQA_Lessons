from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu(user):
    text = f"--= Главное меню =--"
    keyboard = InlineKeyboardMarkup()
    keyboard.row(InlineKeyboardButton('Заказать пиццу', callback_data='order_pizza'),
                 InlineKeyboardButton('История заказов', callback_data='history'))
    keyboard.row(InlineKeyboardButton('Меню аккаунта', callback_data='account'))
    keyboard.row(InlineKeyboardButton('Документы', callback_data='documents'),
                 InlineKeyboardButton('О нас', callback_data='about'))

    user.send_message(text, keyboard)
    user.save_next_message_handler(main_menu_handler)


def main_menu_handler(user, data):
    menus = {
        'order_pizza': order_pizza_menu,
        'history': history_menu,
        'account': account_menu
    }
    menus[data](user)


def account_menu(user):
    text = f"--= Главное меню =--\n" \
           f"{user.username} (phone: {user.phone})"
    keyboard = InlineKeyboardMarkup()
    keyboard.row(InlineKeyboardButton('Изменить никнейм', callback_data='nickname_change'),
                 InlineKeyboardButton('Изменить телефон', callback_data='phone_change'))
    keyboard.row(InlineKeyboardButton('Изменить email', callback_data='email_change'))
    keyboard.row(InlineKeyboardButton('Назад', callback_data='back'))

    user.send_message(text, keyboard)
    user.save_next_message_handler(account_menu_handler)


def account_menu_handler(user, data):
    {
        'nickname_change': nickname_change_menu,
        'phone_change': phone_change_menu,
        'back': lambda user_: main_menu(user_),
    }[data](user)


def nickname_change_menu(user):
    user.send_message('Введите новый никнейм: ')
    user.save_next_message_handler(nickname_change_menu_handler)


def nickname_change_menu_handler(user, text):
    if 4 <= len(text) <= 20:
        user.save_username(text)
        main_menu(user)
    else:
        user.send_message('Ваш никнейм не подходит. Отправьте новый')


def phone_change_menu(user):
    pass


def order_pizza_menu(user):
    pass


def history_menu(user):
    pass


HANDLERS = [main_menu_handler, account_menu_handler, nickname_change_menu_handler]
