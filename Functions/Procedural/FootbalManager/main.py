def input_int(question, error_message='Вы ввели не число. Попробуйте еще.', stop_words=[]):
    while True:
        number_str = input(question)  # '12'
        if number_str in stop_words:
            return number_str

        if number_str.isdigit():
            return int(number_str)
        else:
            print(error_message)


def input_strings_list(question, input_question='Введите число ', min_len=0, max_len=100, stop_words=['stop', 'стоп'], numeration=False):
    print(question)
    strings = []
    numer = 1
    while True:
        if numeration:
            string = input_string(f'{input_question} №{numer}: ', min_len, max_len, stop_words=stop_words)
        else:
            string = input_string(f'{input_question}: ', min_len, max_len, stop_words=stop_words)

        if string in stop_words:
            break
        else:
            strings.append(string)
        numer += 1
    return strings


def input_string(question, min_length=0, max_length=100, only_letters=False, invalid_symbols=[], valid_symbols=[], return_lower=False, stop_words=[]):
    while True:
        ans = input(question)  # 'sdasdfsfgdgsdags@dgsdf'
        if return_lower:
            ans = ans.lower()

        if ans in stop_words:
            return ans

        if min_length <= len(ans) <= max_length:
            if only_letters:
                users_invalid_syms = []
                for letter in ans:
                    if not (letter.isalpha() or letter in valid_symbols):
                        users_invalid_syms.append(letter)

                if len(users_invalid_syms) == 0:
                    return ans
                else:
                    print('Найдены недопустимые символы: ', users_invalid_syms)
            else:
                users_invalid_syms = []
                for symbol in invalid_symbols:
                    if symbol in ans:
                        users_invalid_syms.append(symbol)

                if len(users_invalid_syms) == 0:
                    return ans
                else:
                    print('Найдены недопустимые символы: ', users_invalid_syms)
        else:
            print(f'Слово не подходит по длинне ({min_length} - {max_length})')


def create_team_menu(clubs):
    new_club = {
        'name': '',
        'total_cost': 0,
        'players_amount': 0,
        'city': '',
        'uniform_colors': []
    }
    result = edit_club_menu(new_club, cancel=True)
    if result != 'cancel' and result != 'delete':
        clubs.append(new_club)


def edit_club_menu(club, cancel=False):
    while True:
        print('----= Редактирование клуба =----')
        print(f"1 - Название:    {club['name']}\n"
              f"2 - Цена:        {club['total_cost']}\n"
              f"3 - Игроков:     {club['players_amount']}\n"
              f"4 - Город:       {club['city']}\n"
              f"5 - Цвета:       {club['uniform_colors']}\n"
              f"0 - назад\n")
        if cancel:
            print('6 - отмена')
        print('10 - удалить')

        choice = input('Ваш выбор: ')
        if choice == '1':
            club['name'] = input_string('Введите название команды: ', 3, 70, valid_symbols=[' '], only_letters=True, return_lower=True)
        elif choice == '2':
            club['total_cost'] = input_int('Введите цену клуба: ')
        elif choice == '3':
            club['players_amount'] = input_int('Количество игроков: ')
        elif choice == '4':
            club['city'] = input_string('Введите город: ', 3, 30, only_letters=True, return_lower=True)
        elif choice == '5':
            club['uniform_colors'] = input_strings_list('Введите список форм', 'форма', min_len=5, max_len=60, numeration=True)
        elif choice == '0':
            break
        elif choice == '6' and cancel:
            return 'cancel'
        elif choice == '10':
            if input('Вы уверены? (y/n)') == 'y':
                return 'delete'


def choose_club_menu(clubs):
    print('0 - назад')
    n = 1
    for club in clubs:
        print(f'{n} - {club["name"]}')
        n += 1

    n = input_int('Выберите номер клуба: ')
    if n == 0:
        return None
    index = n - 1
    if 0 <= index < len(clubs):
        club = clubs[index]
        return club
    else:
        print('Такого клуба нету')
        return None


def start_club_edit_menu(clubs):
    club = choose_club_menu(clubs)
    if club:
        result = edit_club_menu(club)
        if result == 'delete':
            clubs.remove(club)


def main_menu(clubs):
    while True:
        print('--= Main menu =--')
        print('1 - добавить клуб\n'
              '2 - редактировать клуб\n'
              '3 - просмотреть таблицу клубов\n'
              '3 - статистика\n'
              '4 - игры\n'
              '5 - выход')

        choice = input('Ваш выбор: ')
        if choice == '1':
            create_team_menu(clubs)
        elif choice == '2':
            start_club_edit_menu(clubs)
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass


def create_clubs():
    clubs = [
        {
            'name': 'Barcelona',
            'total_cost': 120495091,
            'players_amount': 35,
            'city': 'Barcelona',
            'uniform_colors': ['blue-red-black', 'pink-blank']
        },
        {
            'name': 'Manchester City',
            'total_cost': 120591096,
            'players_amount': 45,
            'city': 'Manchester',
            'uniform_colors': ['blue-white-black', 'pink']
        },
    ]
    return clubs


def main():
    clubs = create_clubs()
    main_menu(clubs)


main()
