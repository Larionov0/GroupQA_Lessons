posts = [
    {
        'name': '',
        'text': '',
        'tags': [],
        'comments': [],
        'likes': 0,
        'dislikes': 0
    },
    {
        'name': '',
        'text': '',
        'tags': [],
        'comments': [],
        'likes': 0,
        'dislikes': 0
    },
]

users = [
    {
        'username': 'Bobik',
        'password': 'aflkjalgnk',
        'email': 'bob@gmail.com',
        'bio': ''
    },
    {
        'username': 'Kurup4ik',
        'password': 'password',
        'email': 'kur@gmail.com',
        'bio': ''
    },
    {
        'username': 'Alabchik',
        'password': 'password',
        'email': 'ala@gmail.com',
        'bio': ''
    }
]

while True:
    for user in users:
        print(user)
    print('---= Внешнее меню =---\n'
          '1 - зарегистрироваться\n'
          '2 - авторизироваться\n'
          '3 - выйти из программы\n')
    choice = input('Ваш выбор: ')
    if choice == '1':
        name = 'Имя'
        password = 'Пароль'
        password_a = 'Пароль'
        mail = 'мейл@gmail.com'
        while True:
            print('---= Регистрация =---\n'
                  f'1 - имя:                {name} \n'
                  f'2 - пароль:             {"*" * len(password)}\n'
                  f'3 - подтвердить пароль: {"*" * len(password_a)}\n'
                  f'4 - mail:               {mail}\n'
                  f'5 - зарегистрироваться\n'
                  f'6 - назад')

            choice = input('Ваш выбор:')
            if choice == '1':
                new_name = input('Введите новое имя: ')
                if 50 >= len(new_name) >= 5:
                    name = new_name
                else:
                    print('Имя не подходит по длине (надо от 5 до 50 символов)')

            elif choice == '2':
                new_password = input('Введите новый пароль: ')
                if 50 >= len(new_password) >= 6:
                    password = new_password
                else:
                    print('Пароль не подходит по длине (надо от 6 до 50 символов)')

            elif choice == '3':
                new_password_a = input('Подтвердите пароль: ')
                if new_password_a == password:
                    password_a = new_password_a
                else:
                    print('Пароли не совпадают')

            elif choice == '4':
                new_mail = input('Введите новый mail: ')
                if 100 >= len(new_mail) >= 5:
                    if '@' in new_mail and ' ' not in new_mail:
                        mail = new_mail
                    else:
                        print('Это не mail')
                else:
                    print('mail не подходит по длине (надо от 5 до 50 символов)')

            elif choice == '5':
                if password == password_a:
                    # проверить, а нету ли уже юзера с таким юзернеймом
                    is_username_exists = False

                    for user in users:
                        if user['username'] == name:
                            is_username_exists = True
                            break

                    if is_username_exists:
                        print('Такой пользователь уже существует! :(\n'
                              'Попробйте другое имя')
                    else:
                        new_user = {
                            'username': name,
                            'password': password,
                            'email': mail,
                            'bio': ''
                        }

                        users.append(new_user)
                        print('Вы зарегистрированы! :)')
                        break
                else:
                    print('Вы не подтвердили пароль!')

    elif choice == '2':
        name = 'Имя'
        password = 'Пароль'
        while True:
            print('---= Регистрация =---\n'
                  f'1 - имя:                {name} \n'
                  f'2 - пароль:             {"*" * len(password)}\n'
                  f'3 - авторизироваться\n'
                  f'4 - назад')

            choice = input('Ваш выбор:')
            if choice == '1':
                new_name = input('Введите имя: ')
                if 50 >= len(new_name) >= 5:
                    name = new_name
                else:
                    print('Имя не подходит по длине (надо от 5 до 50 символов)')

            elif choice == '2':
                new_password = input('Введите пароль: ')
                if 50 >= len(new_password) >= 6:
                    password = new_password
                else:
                    print('Пароль не подходит по длине (надо от 6 до 50 символов)')

            elif choice == '3':
                a_user = None

                for user in users:
                    if user['username'] == name and user['password'] == password:
                        a_user = user
                        break

                if a_user is None:
                    print('Ошибка авторизации')
                else:
                    print('Вы авторизированы! :)')
                    print(a_user)

                    while True:
                        print(f'Вы вошли как {a_user["username"]}')
                        choice = input('Ваш выбор: ')

    elif choice == '3':
        break
