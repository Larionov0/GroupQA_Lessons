import colorama
import time


def translate_color(color):
    dict_color = {'синий': colorama.Fore.BLUE, 'красный': colorama.Fore.RED, 'зеленый': colorama.Fore.GREEN,
                  'черный': colorama.Fore.BLACK, 'белый': colorama.Fore.WHITE, 'желтый': colorama.Fore.YELLOW,
                  'розовый': colorama.Fore.MAGENTA, 'голубой': colorama.Fore.CYAN}
    return dict_color[color]


class Messenger:
    def __init__(self, color: str, dashes_amount: int, messages_amount: int, filename, save_datetime: bool,
                 messages_history: list[str] = None):
        self.color = color  # отвечает за цвет выводимого текста - использовать colorama.
        self.dashes_amount = dashes_amount  # количество черточек "-" перед выводом
        self.messages_history = messages_history if messages_history else []  # Список последних сообщений.
        self.messages_amount = messages_amount  # Это количество сообщений для запоминания
        self.filename = filename  # имя файла
        self.save_datetime = save_datetime  # Если = True, нужно записывать в файл дату и время в каждом сообщении

    def print(self, text):
        """Это главный метод нашего Мессенджера.
        Он должен выводить сообщение message на экран, но помимо этого должен также запоминать его, возможно сохранять в файл, и тд.
        В общем, делать всё, что описано выше в параметрах."""
        save_data = f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}' if self.save_datetime else ''
        text_for_save = f'{save_data}' + '\n' + f'{self.dashes_amount * "-"}{text}'
        if self.messages_amount == 0:
            pass
        else:
            self.messages_history.append(text)
            if len(self.messages_history) >= self.messages_amount:
                self.messages_history.pop(0)

        if self.filename is not None and self.filename[-3:] == 'txt':
            with open(self.filename, 'at', encoding='utf-8') as file:
                file.write(text_for_save + '\n\n')

        print(f'{translate_color(self.color)}' + text_for_save + colorama.Style.RESET_ALL)

    def show_history(self):
        """
        Нужно вывести на экран все сообщения, сохраненные в истории.
        Формат вывода выбирайте сами) Только цвет должен быть соответствующий нашему мессенджеру.
        """
        for txt in self.messages_history:
            print(f'{translate_color(self.color)}' + txt + colorama.Style.RESET_ALL)

    def show_archive(self):
        """
        Нужно просто вывести всё, что было в файле. Если при создании мессенджера filename=None, выдать ошибку,
        что мессенджер не имеет информации про архив
        """
        if self.filename is None:
            print('Error: messenger not information about archive')
        else:
            with open(self.filename, 'rt', encoding='utf-8') as file:
                print(translate_color(self.color) + file.read() + colorama.Style.RESET_ALL)


def main():
    color_for_text = 'синий'
    dashes_for_text = 0
    history_amount = 0
    name_file_text = None
    data_for_save_in_text = False
    history = []

    while True:
        messenger = Messenger(color_for_text, dashes_for_text, history_amount, name_file_text, data_for_save_in_text,
                              messages_history=history)
        print(f'{"*" * 5}\n{messenger.__dict__}\n{"*" * 5}\n')
        print(f'-=Меню=-\n'
              f'1. Настройка перед вводом текста\n'
              f'2. Вводить текст\n'
              f'3. Смотреть текущую историю\n'
              f'4. Смотреть весь файл\n'
              f'0. Exit\n')

        choice = input('Введите номер меню: ')

        if choice == '1':
            input_color = input('\nВвести цвет текста или пропустить - "0": ')
            color_for_text = input_color if input_color in ['синий', 'красный', 'зеленый',
                                                            'черный', 'белый', 'желтый',
                                                            'розовый', 'голубой'] else color_for_text
            dashes = input('\nВведите количество черточек перед текстом '
                           'или пропустить(если не число): ')
            dashes_for_text = int(dashes) if dashes.isdigit() else dashes_for_text
            amount = input('\nВведите число для сохранения количества сообщений'
                           'или пропустить(если не число): ')
            history_amount = int(amount) if amount.isdigit() else history_amount
            name = input('\nВведите название файла или пропустить - "0": ')
            name_file_text = name if name != '0' and name[-3:] == 'txt' else name_file_text
            save_ = input('\nВводить текущее время? "y" - да, "n" - нет: ')
            data_for_save_in_text = True if save_ == 'y' else False if save_ == 'n' else data_for_save_in_text

        if choice == '2':
            num = input('\nВведите число сколько будете вводить строк текста: ')
            for _ in range(int(num) if num.isdigit() else 0):
                messenger.print(input())

        if choice == '3':
            messenger.show_history()

        if choice == '4':
            try:
                messenger.show_archive()
            except Exception as exc:
                print(f'\n{exc}\nФайл не найден, так как вы еще ничего не вводили!')

        if choice == '0':
            break


def main2():
    messenger = Messenger('синий', 2, 10, 'text.txt', True)
    messenger.print('Привет, мир')
    messenger.print('Пока')
    messenger.show_history()
    print('----')
    messenger.show_archive()


if __name__ == '__main__':
    main2()
