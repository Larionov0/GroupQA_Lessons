from db.db import connect
from business_handlers import HANDLERS
from tools.pizza_sizes import pizza_sizes


class User:
    table = 'User_'
    columns = ['id', 'username', 'phone', 'email', 'cur_cart_id', 'bot_message_id', 'next_message_handler',
               'cur_pizza_id', 'cur_chosen_size', 'cur_chosen_side']

    def __init__(self, bot, id, username, phone, email, cur_cart_id, bot_message_id, next_message_handler, cur_pizza_id,
                 cur_chosen_size, cur_chosen_side):
        self.bot = bot
        self.id = id
        self.username = username
        self.phone = phone
        self.email = email
        self.cur_cart_id = cur_cart_id
        self.bot_message_id = bot_message_id
        self.next_message_handler = next_message_handler  # index of handler in list
        self.cur_pizza_id = cur_pizza_id
        self.cur_chosen_size = cur_chosen_size
        self.cur_chosen_side = cur_chosen_side

    @property
    def cur_chosen_size_name(self):
        return pizza_sizes[int(self.cur_chosen_size)]

    def save_username(self, new_username):
        self.username = new_username
        query = f"UPDATE {self.table} \n" \
                f"SET username = ? \n" \
                f"WHERE id = {self.id}"
        conn, cursor = connect()
        cursor.execute(query, (new_username,))
        conn.commit()

    @property
    def chat_id(self):
        return self.id

    @classmethod
    def get_by_id(cls, chat_id, bot):
        conn, cursor = connect()
        query = f"SELECT {','.join(cls.columns)} FROM {cls.table} WHERE id = {chat_id}"
        cursor.execute(query)
        table = cursor.fetchall()
        if len(table) == 0:
            raise UserNotFoundError(chat_id)

        kwargs = {column: value for column, value in zip(cls.columns, table[0])}
        return cls(bot=bot, **kwargs)

    @classmethod
    def create_user_if_it_is_not_in_db(cls, chat_id):
        conn, cursor = connect()
        cursor.execute(f'SELECT id FROM {cls.table} WHERE id={chat_id}')
        table = cursor.fetchall()
        if len(table) == 0:
            cls.create_default_user(chat_id, conn, cursor)

    @classmethod
    def create_default_user(cls, chat_id, conn, cursor):
        cursor.execute(f"INSERT INTO {cls.table} (id, username) VALUES ({chat_id}, 'New user')")
        conn.commit()

    def save_next_message_handler(self, handler):
        index = HANDLERS.index(handler)
        query = f"UPDATE {self.table}\n" \
                f"SET next_message_handler = {index}\n" \
                f"WHERE id={self.id}"
        conn, cursor = connect()
        cursor.execute(query)
        conn.commit()
        self.next_message_handler = index

    def send_message(self, message, keyboard=None):
        if self.bot_message_id is None:
            message = self.bot.send_message(self.id, message, reply_markup=keyboard)
            self.save_bot_message_id(message.message_id)
        else:
            try:
                message = self.bot.edit_message_text(message, self.chat_id, self.bot_message_id, reply_markup=keyboard)
            except Exception as exc:
                if not 'message is not modified' in exc.description.lower():
                    raise exc

    def save_bot_message_id(self, bot_message_id):
        query = f"UPDATE {self.table}\n" \
                f"SET bot_message_id = {bot_message_id}\n" \
                f"WHERE id={self.id}"
        conn, cursor = connect()
        cursor.execute(query)
        conn.commit()
        self.bot_message_id = bot_message_id
