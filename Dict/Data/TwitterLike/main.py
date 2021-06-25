from os import system

DASHES = 30

posts = [
    {
        'name': 'Про черешню',
        'text': 'Вчера купил черешню\n'
                'Пока кислая, но неплохо.',
        'tags': [],
        'comments': [],
        'likes': [],
        'dislikes': [],
        'author': None
    },
    {
        'name': 'Я люблю пиццу',
        'text': 'Только не кладите в нее морепродукты\n'
                'Или ананасы\n'
                'Я их не люблю',
        'tags': [],
        'comments': [],
        'likes': [],
        'dislikes': [],
        'author': None
    },
]

users = [
    {
        'username': 'Bobik',
        'password': '123456',
        'email': 'bob@gmail.com',
        'bio': '',
        'posts': [],
        'following': []
    },
    {
        'username': 'Kurup4ik',
        'password': 'password',
        'email': 'kur@gmail.com',
        'bio': '',
        'posts': [],
        'following': []
    },
    {
        'username': 'Alabchik',
        'password': 'password',
        'email': 'ala@gmail.com',
        'bio': '',
        'posts': [],
        'following': []
    },
    {
        'username': 'KarBoban',
        'password': 'password',
        'email': 'aa@gmail.com',
        'bio': '',
        'posts': [],
        'following': []
    },
    {
        'username': 'AlanrBober',
        'password': 'password',
        'email': 'aaa@gmail.com',
        'bio': '',
        'posts': [],
        'following': []
    }
]

bobik = users[0]

bobik['posts'].append(posts[0])
posts[0]['author'] = bobik

bobik['posts'].append(posts[1])
posts[1]['author'] = bobik

posts[0]['likes'].append(users[-1])

while True:
    for user in users:
        print(user)
    system('cls')
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
            system('cls')
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
            system('cls')
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

                for user in users:  # ищем пользователя с таким юзернеймом и паролем
                    if user['username'] == name and user['password'] == password:
                        a_user = user
                        break

                if a_user is None:
                    print('Ошибка авторизации')
                else:
                    print('Вы авторизированы! :)')

                    while True:
                        system('cls')
                        print(f'Вы вошли как {a_user["username"]}')
                        print('1 - Моя лента\n'
                              '2 - Мой аккаунт\n'
                              '3 - Настройки\n'
                              '4 - Искать людей\n'
                              '5 - Рекомендации\n'
                              '6 - выход из аккаунта')
                        choice = input('Ваш выбор: ')

                        if choice == '1':
                            pass
                        elif choice == '2':
                            while True:
                                system('cls')
                                print('---= Ваш аккаунт =---')
                                print(f'Пользователь {a_user["username"]}\n'
                                      f'Bio: {a_user["bio"]}')
                                print('1 - просмотреть посты\n'
                                      '2 - добавить пост\n'
                                      '3 - редактировать профиль\n'
                                      '0 - назад')

                                choice = input('Ваш выбор: ')

                                if choice == '0':
                                    break

                                if choice == '1':
                                    while True:
                                        system('cls')
                                        print('Ваши посты: ')
                                        n = 1
                                        for post in a_user['posts']:
                                            if a_user in post['likes']:  # проверяем, лайкал ли наш юзер этот пост. ДЛя того чтобы вывести пометочку в случае если да
                                                mark = '♥'
                                            else:
                                                mark = ' '

                                            print(f'{"=" * DASHES}\n'
                                                  f'Пост №{n} : {post["name"]}\n'
                                                  f'{"-" * DASHES}\n'
                                                  f'{post["text"]}\n'
                                                  f'{"-" * DASHES}\n'
                                                  f'Likes: {len(post["likes"])} {mark}  | Dislikes: {len(post["dislikes"])}\n'
                                                  f'{"=" * DASHES}')
                                            print('\n')
                                            n += 1
                                        print('0 - назад')
                                        number = int(input('Выберите пост для детального просмотра: '))

                                        if number == 0:
                                            break

                                        index = number - 1
                                        if 0 <= index < len(a_user['posts']):
                                            post = a_user['posts'][index]
                                            while True:
                                                if a_user in post['likes']:  # проверяем, лайкал ли наш юзер этот пост. ДЛя того чтобы вывести пометочку в случае если да
                                                    mark = '♥'
                                                else:
                                                    mark = ' '

                                                system('cls')
                                                print(f'{"=" * DASHES}\n'
                                                      f'{post["name"]}\n'
                                                      f'{"-" * DASHES}\n'
                                                      f'{post["text"]}\n'
                                                      f'{"-" * DASHES}\n'
                                                      f'Likes: {len(post["likes"])} {mark} | Dislikes: {len(post["dislikes"])}\n'
                                                      f'{"=" * DASHES}')
                                                print("Комменты: ", post['comments'])
                                                print('Теги: ', post['tags'])

                                                print('1 - редактировать имя\n'
                                                      '2 - редактировать пост\n'
                                                      '3 - оставить комментарий\n'
                                                      '4 - удалить пост\n'
                                                      '5 - лайкнуть\n'
                                                      '6 - дизлайкнуть\n'
                                                      '0 - назад')
                                                choice = input('Ваш выбор: ')
                                                if choice == '0':
                                                    break
                                                elif choice == '1':
                                                    print('Введите название поста')
                                                    post['name'] = input()
                                                elif choice == '2':
                                                    print('Введите новый текст поста')
                                                    post['text'] = input()
                                                elif choice == '4':
                                                    a_user['posts'].remove(post)
                                                    posts.remove(post)
                                                    break
                                                elif choice == '5':
                                                    if a_user in post['likes']:
                                                        post['likes'].remove(a_user)
                                                    else:
                                                        post['likes'].append(a_user)
                                                elif choice == '6':
                                                    if a_user in post['dislikes']:
                                                        post['dislikes'].remove(a_user)
                                                    else:
                                                        post['dislikes'].append(a_user)
                                        else:
                                            print('Нету такого поста!')

                                elif choice == '2':
                                    post = {
                                        'name': 'Новый пост',
                                        'text': 'Текст поста',
                                        'tags': [],
                                        'comments': [],
                                        'likes': [],
                                        'dislikes': [],
                                        'author': a_user
                                    }
                                    posts.append(post)
                                    a_user['posts'].append(post)

                                    while True:
                                        if a_user in post['likes']:  # проверяем, лайкал ли наш юзер этот пост. ДЛя того чтобы вывести пометочку в случае если да
                                            mark = '♥'
                                        else:
                                            mark = ' '

                                        system('cls')
                                        print(f'{"=" * DASHES}\n'
                                              f'{post["name"]}\n'
                                              f'{"-" * DASHES}\n'
                                              f'{post["text"]}\n'
                                              f'{"-" * DASHES}\n'
                                              f'Likes: {len(post["likes"])} {mark} | Dislikes: {len(post["dislikes"])}\n'
                                              f'{"=" * DASHES}')
                                        print("Комменты: ", post['comments'])
                                        print('Теги: ', post['tags'])

                                        print('1 - редактировать имя\n'
                                              '2 - редактировать пост\n'
                                              '3 - оставить комментарий\n'
                                              '4 - удалить пост\n'
                                              '5 - лайкнуть\n'
                                              '6 - дизлайкнуть\n'
                                              '0 - назад')
                                        choice = input('Ваш выбор: ')
                                        if choice == '0':
                                            break
                                        elif choice == '1':
                                            print('Введите название поста')
                                            post['name'] = input()
                                        elif choice == '2':
                                            print('Введите новый текст поста')
                                            post['text'] = input()
                                        elif choice == '4':
                                            a_user['posts'].remove(post)
                                            posts.remove(post)
                                            break
                                        elif choice == '5':
                                            if a_user in post['likes']:
                                                post['likes'].remove(a_user)
                                            else:
                                                post['likes'].append(a_user)
                                        elif choice == '6':
                                            if a_user in post['dislikes']:
                                                post['dislikes'].remove(a_user)
                                            else:
                                                post['dislikes'].append(a_user)

                        elif choice == '4':
                            username_part = ''
                            ok_users = []
                            while True:
                                system('cls')
                                print('---= Поиск друзей =---')
                                print('Подходящие пользователи:')
                                n = 1
                                for user in ok_users:
                                    print(f'---| №{n} {user["username"]} ({len(user["posts"])} постов) |---')
                                    n += 1

                                print(f'Введенное имя: {username_part}\n'
                                      f'1 - Изменить имя\n'
                                      f'2 - Поиск\n'
                                      f'3 - Подсказка\n'
                                      f'0 - Назад\n')


                                choice = input('Ваш выбор: ')
                                if choice == '0':
                                    break
                                elif choice == '1':
                                    username_part = input('Введите имя (или его часть): ')
                                elif choice == '2':
                                    # Обновляем список подходящих пользователей в ok_users
                                    ok_users.clear()

                                    for user in users:  # фильтруем подходящих по имени пользователей
                                        if username_part.lower() in user['username'].lower():
                                            ok_users.append(user)
                                elif choice == '3':
                                    print('! Если готовы выбрать пользователя, \n'
                                          'введите "u<n>" , где <n> - номер пользователя\n'
                                          '(Например: "u4")')
                                    input('Жми <Enter>')
                                elif choice[0] == 'u':
                                    right_side = choice[1:]
                                    index = int(right_side) - 1

                                    user = ok_users[index]

                                    while True:
                                        system('cls')
                                        info = ''
                                        if a_user in user['following']:
                                            info += 'Подписан на вас\n'
                                        if user in a_user['following']:
                                            info += 'Вы подписаны\n'

                                        print('--= Просмотр страницы =--')
                                        print(f'Пользователь {user["username"]}\n'
                                              f'Bio: {user["bio"]}')
                                        print(info)
                                        print('1 - просмотреть посты\n'
                                              '2 - подписаться\n'
                                              '0 - назад\n')
                                        choice = input('Ваш выбор: ')

                                        if choice == '0':
                                            break
                                        elif choice == '2':
                                            if user not in a_user['following']:
                                                a_user['following'].append(user)
                                            else:
                                                input('Вы и так подписаны на него!')

    elif choice == '3':
        break
