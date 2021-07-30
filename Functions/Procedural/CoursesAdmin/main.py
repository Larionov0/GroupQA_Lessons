import datetime


clients = [
    {
        'name': '',
        'surname': '',
        'balance': ''
    }
]

teachers = [
    {
        'name': '',
        'surname': '',
        'courses': [],
        'master_koef': 1
    }
]

courses = [
    {
        'name': 'C bases',
        'description': '',
        'teacher_price': 200,
        'client_price': 300
    }
]

groups = [
    {
        'number': 1,
        'students': [],
        'teacher': None,
        'course': courses[0]
    }
]

lessons = [
    {
        'date': datetime.date(2021, 7, 30),
        'time': datetime.time(hour=16),
        'duration': datetime.timedelta(hours=1.5),
        'present_students': [],
        'theme': '',
        'group': groups[0]
    }
]


def edit_client_menu(client, clients):
    while True:
        print(f'---= Редактирование клиента =---\n'
              f'{client}\n\n'
              f'0 - назад\n'
              f'1 - имя\n'
              f'2 - фамилия\n'
              f'3 - баланс\n'
              f'4 - удалить')
        choice = input('Ваш выбор: ')
        if choice == '0':
            return
        elif choice == '1':
            client['name'] = input('New name: ')
        elif choice == '2':
            client['surname'] = input('New surname: ')
        elif choice == '3':
            client['balance'] = int(input('New balance'))
        elif choice == '4':
            clients.remove(client)
            return


def clients_menu(clients, groups, lessons):
    while True:
        print('---= Clients menu =---\n'
              '0 - назад\n'
              '1 - просмотреть клиентов\n'
              '2 - редактировать клиента\n'
              '3 - создать клиента')
        choice = input('Что будем делать: ')
        if choice == '0':
            return
        elif choice == '1':
            pass
        elif choice == '2':
            n = 1
            for client in clients:
                print(f'{n} - {client["name"]} {client["surname"]}')
                n += 1

            number = int(input('Ваш выбор: '))
            index = number - 1

            client = clients[index]
            edit_client_menu(client, clients)

        elif choice == '3':
            new_client = {
                    'name': '',
                    'surname': '',
                    'balance': ''
                }
            clients.append(new_client)
            edit_client_menu(new_client, clients)


def main_menu(clients, teachers, courses, groups, lessons):
    while True:
        print('---= Main menu =---\n'
              '1 - клиенты\n'
              '2 - учителя\n'
              '3 - курсы\n'
              '4 - группы\n'
              '5 - уроки')

        choice = input('Ваш выбор: ')
        if choice == '1':
            clients_menu(clients, groups, lessons)
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass


main_menu(clients, teachers, courses, groups, lessons)
