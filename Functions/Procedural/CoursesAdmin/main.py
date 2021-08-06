import datetime


clients_columns = [
    {
        'name': 'name',
        'type': 'str',
        'validators': [
            {
                'type': 'check_min_length',
                'min_length': 3
            },
            {
                'type': 'check_max_length',
                'max_length': 20
            },
            {
                'type': 'check_only_letters',
                'exceptional_symbols': []
            }
        ]
    },
    {
        'name': 'surname',
        'type': 'str',
        'validators': [
            {
                'type': 'check_min_length',
                'min_length': 3
            },
            {
                'type': 'check_max_length',
                'max_length': 40
            },
            {
                'type': 'check_only_letters',
                'exceptional_symbols': []
            }
        ]
    },
    {
        'name': 'balance',
        'type': 'int',
        'validators': [
            {
                'type': 'check_min',
                'min': 3
            },
            {
                'type': 'check_max',
                'max': 40
            }
        ]
    }
]

courses_columns = [
    {
        'name': 'name',
        'type': 'str'
    },
    {
        'name': 'description',
        'type': 'str'
    },
    {
        'name': 'teacher_price',
        'type': 'int'
    },
    {
        'name': 'client_price',
        'type': 'int'
    },
]


teachers_columns = [
    {
        'name': 'name',
        'type': 'str'
    },
    {
        'name': 'surname',
        'type': 'str'
    },
    {
        'name': 'courses',
        'type': 'str'
    },
    {
        'name': 'master_koef',
        'type': 'int'
    },
]

groups_columns = [
    {
        'name': 'number',
        'type': 'int'
    },
    {
        'name': 'students',
        'type': 'str'
    },
    {
        'name': 'teacher',
        'type': 'str'
    },
    {
        'name': 'course',
        'type': 'str'
    },
]


clients = [
    {
        'name': 'Bob',
        'surname': 'Bobenko',
        'balance': 200
    },
    {
        'name': 'Katia',
        'surname': 'Vasilenko',
        'balance': 400
    }
]

teachers = [
    {
        'name': 'Teacher',
        'surname': 'Bober',
        'courses': 'Python, C, math',  # []
        'master_koef': 2
    }
]

courses = [
    {
        'name': 'C bases',
        'description': 'best C course',
        'teacher_price': 200,
        'client_price': 300
    },
    {
        'name': 'Python bases',
        'description': 'best Py course',
        'teacher_price': 300,
        'client_price': 400
    },
    {
        'name': 'Math',
        'description': 'best C course',
        'teacher_price': 100,
        'client_price': 200
    },
]

groups = [
    {
        'number': 1,
        'students': '[]',  # []
        'teacher': 'None',  # None
        'course': 'courses[0]'  # courses[0]
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


def input_int(question, error_message='Вы ввели не число. Попробуйте еще.', stop_words=[]):
    while True:
        number_str = input(question)  # '12'
        if number_str in stop_words:
            return number_str

        if number_str.isdigit():
            return int(number_str)
        else:
            print(error_message)


def input_column(column):
    if column['type'] == 'str':
        value = input(f'Введите {column["name"]}: ')
    elif column['type'] == 'int':
        value = input_int(f'Введите {column["name"]}: ')
    return value


def edit_object_menu(object_name, object, columns, data_list):  # 'Client', {'name': '..', 'surname': '..'}, [..], [clients]}
    while True:
        print(f"--= Редактируем {object_name} =--")
        print(object)
        print('0 - back')
        n = 1
        for column in columns:
            print(f'{n} - {column["name"]}')
            n += 1
        choice = int(input('Ваш выбор: '))
        if choice == 0:
            return

        index = choice - 1
        column = columns[index]

        value = input_column(column)
        object[column['name']] = value


def show_data_table(object_name, data_list, columns):
    sample = '|'
    columns_names = []
    for column in columns:
        sample += '%-15s|'
        columns_names.append(column['name'])
    headers = sample % tuple(columns_names)
    print(headers)
    print('-' * (16 * len(columns) + 1))

    for dct in data_list:  # {'name': 'Bob','surname': 'Bobenko','balance': 500}
        row_text = sample % tuple(dct.values())
        print(row_text)
    print('-' * (16 * len(columns) + 1))


def work_with_objects_constructor_menu(object_name, data_list, columns):
    while True:
        print(f'---= {object_name} =---')
        print('0 - назад\n'
              f'1 - просмотреть {object_name}\n'
              f'2 - редактировать {object_name}\n'
              f'3 - создать {object_name}\n')
        choice = input('Ваш выбор: ')
        if choice == '0':
            return
        elif choice == '1':
            show_data_table(object_name, data_list, columns)
        elif choice == '2':
            print('0 - назад')
            n = 1
            for object in data_list:
                print(f'{n} - {object["name"]}')
                n += 1

            number = int(input('Ваш выбор: '))
            index = number - 1

            object = data_list[index]
            edit_object_menu(object_name, object, columns, data_list)
        elif choice == '3':
            pass


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
            work_with_objects_constructor_menu('client', clients, clients_columns)
        elif choice == '2':
            work_with_objects_constructor_menu('teacher', teachers, teachers_columns)
        elif choice == '3':
            work_with_objects_constructor_menu('course', courses, courses_columns)
        elif choice == '4':
            work_with_objects_constructor_menu('group', groups, groups_columns)
        elif choice == '5':
            pass


main_menu(clients, teachers, courses, groups, lessons)


#
# def edit_client_menu(client, clients):
#     while True:
#         print(f'---= Редактирование клиента =---\n'
#               f'{client}\n\n'
#               f'0 - назад\n'
#               f'1 - имя\n'
#               f'2 - фамилия\n'
#               f'3 - баланс\n'
#               f'4 - удалить')
#         choice = input('Ваш выбор: ')
#         if choice == '0':
#             return
#         elif choice == '1':
#             client['name'] = input('New name: ')
#         elif choice == '2':
#             client['surname'] = input('New surname: ')
#         elif choice == '3':
#             client['balance'] = int(input('New balance'))
#         elif choice == '4':
#             clients.remove(client)
#             return
#
#
# def choose_client_menu(clients):
#     print('0 - назад')
#     n = 1
#     for client in clients:
#         print(f'{n} - {client["name"]} {client["surname"]}')
#         n += 1
#
#     number = int(input('Ваш выбор: '))
#     index = number - 1
#
#     client = clients[index]
#     edit_client_menu(client, clients)
#
#
# def create_client_menu(clients):
#     new_client = {
#         'name': '',
#         'surname': '',
#         'balance': ''
#     }
#     clients.append(new_client)
#     edit_client_menu(new_client, clients)
#
#
# def clients_menu(clients, groups, lessons):
#     while True:
#         print('---= Clients menu =---\n'
#               '0 - назад\n'
#               '1 - просмотреть клиентов\n'
#               '2 - редактировать клиента\n'
#               '3 - создать клиента')
#         choice = input('Что будем делать: ')
#         if choice == '0':
#             return
#         elif choice == '1':
#             pass
#         elif choice == '2':
#             choose_client_menu(clients)
#
#         elif choice == '3':
#             create_client_menu(clients)
#
#

#
#
# main_menu(clients, teachers, courses, groups, lessons)
