from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from db.db import connect
from tools.pizza_sizes import pizza_sizes


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
        'order_pizza': choose_pizza_menu,
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


def choose_pizza_menu(user):
    conn, cursor = connect()
    query = "SELECT Pizza.id, Pizza.name, Ingredient.name\n" \
            "FROM Pizza \n" \
            "JOIN IngredientInPizza ON Pizza.id = IngredientInPizza.pizza_id\n" \
            "JOIN Ingredient ON Ingredient.id = IngredientInPizza.ingredient_id\n" \
            "ORDER BY Pizza.id"
    cursor.execute(query)
    table = cursor.fetchall()

    keyboard = InlineKeyboardMarkup()
    last_pizza_id = None
    text = ''
    for row in table + [(-10, '', '')]:
        if row[0] != last_pizza_id:
            if last_pizza_id is not None:
                keyboard.row(InlineKeyboardButton(text[:-2] + ')', callback_data=last_pizza_id))

            text = row[1] + ' ('
            last_pizza_id = row[0]

        text += row[2] + ', '

    keyboard.row(InlineKeyboardButton('Назад', callback_data='back'))
    user.send_message('Виберіть піцу:', keyboard)
    user.save_next_message_handler(choose_pizza_menu_handler)


def choose_pizza_menu_handler(user, data):
    if data == 'back':
        return main_menu(user)

    conn, cursor = connect()
    cursor.execute(f"UPDATE User_ SET cur_pizza_id=? WHERE id={user.id}", (data,))
    conn.commit()
    choose_pizza_size_menu(user, data)


def choose_pizza_size_menu(user, pizza_id):
    conn, cursor = connect()
    query = "SELECT Pizza.name, Ingredient.name, IngredientInPizza.grams\n" \
            "FROM Pizza \n" \
            "JOIN IngredientInPizza ON Pizza.id = IngredientInPizza.pizza_id\n" \
            "JOIN Ingredient ON Ingredient.id = IngredientInPizza.ingredient_id\n" \
            "WHERE Pizza.id = ?"
    cursor.execute(query, (pizza_id,))
    table = cursor.fetchall()

    text = f"Ваша піца: {table[0][0]}\n" \
           f"Інгрідієнти:\n"
    for row in table:
        text += f'- {row[1]} ({row[2]} грам)\n'
    text += f"Розмір: {user.cur_chosen_size_name}\n" \
            f"Борт: пустий"

    keyboard = InlineKeyboardMarkup()
    for size in range(1, 4):
        keyboard.row(InlineKeyboardButton(f'змінити розмір: {pizza_sizes[size]}', callback_data=f"s{size}"))
    # TODO: додати борти піц
    keyboard.row(InlineKeyboardButton(f"Відміна", callback_data='cancel'))
    keyboard.row(InlineKeyboardButton(f"В корзину", callback_data='add'))
    user.send_message(text, keyboard)
    user.save_next_message_handler(choose_pizza_size_menu_handler)


def choose_pizza_size_menu_handler(user, data):
    conn, cursor = connect()

    if data == 'cancel':
        return choose_pizza_menu(user)
    if data == 'add':
        return

    if data[0] == 's':
        new_size = data[1]
        cursor.execute(f'UPDATE User_ SET cur_chosen_size = ? WHERE id={user.id}', (new_size,))
        conn.commit()
        user.cur_chosen_size = new_size
        choose_pizza_size_menu(user, user.cur_pizza_id)


def history_menu(user):
    pass


HANDLERS = [main_menu_handler, account_menu_handler, nickname_change_menu_handler, choose_pizza_menu_handler,
            choose_pizza_size_menu_handler]
