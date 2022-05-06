from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from classes.user import User


class Lobby:
    lobbies = []

    def __init__(self, name, bot, users=None, max_players=2, lobbies_menu=None):
        self.name = name
        self.bot = bot

        if users is None:
            users = []
        self.users = users
        self.max_players = max_players

        self.active_hero_index = 0
        self.lobbies_menu = lobbies_menu

    def __str__(self):
        return f"Лобби '{self.name}' ({len(self.users)}/{self.max_players})"

    @classmethod
    def find_lobby(cls, name):
        for lobby in cls.lobbies:
            if lobby.name == name:
                return lobby

    def enter(self, user):
        if len(self.users) < self.max_players:
            self.users.append(user)
            user.lobby = self

            for user in self.users:
                self.lobby_menu(user)

            if len(self.users) == self.max_players:
                self.start_game()
        else:
            user.resend_message('Не удалось войти, так как лобби заполнено')

    def start_game(self):
        pass

    def lobby_menu(self, main_user):
        text = f'---= Лобби {main_user.lobby.name} =---\n'
        for user in main_user.lobby.users:
            text += f"- {user.username}\n"
        keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)
        keyboard.row(KeyboardButton('выход'))
        main_user.resend_message(text, keyboard)
        self.bot.register_next_step_handler_by_chat_id(main_user.chat_id, self.lobby_menu_handler)

    def lobby_menu_handler(self, message):
        user = User.find_user_and_delete_message(message, self.bot)
        if message.text == 'выход':
            lobby = user.lobby
            user.exit_lobby()
            for l_user in lobby.users:
                self.lobby_menu(l_user)
            self.lobbies_menu(user)
