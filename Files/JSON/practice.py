import datetime
import json


def create_init_data():
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
        },
        {
            'name': 'Alice',
            'surname': 'Burenko',
            'balance': 1500
        }
    ]

    courses = [
        {
            'name': 'C bases',
            'description': 'best C course',
            'payment_koef': 200
        },
        {
            'name': 'Python bases',
            'description': 'best Py course',
            'payment_koef': 300,
        },
        {
            'name': 'Math',
            'description': 'best C course',
            'payment_koef': 100,
        },
    ]

    teachers = [
        {
            'name': 'Teacher',
            'surname': 'Bober',
            'courses': [courses[0], courses[1]],
            'master_koef': 2,
            'salary': 0
        }
    ]

    groups = [
        {
            'number': 1,
            'students': [clients[0], clients[1]],
            'teacher': teachers[0],
            'course': courses[0]
        }
    ]

    lessons = [
        {
            # 'date': datetime.date(2021, 7, 30),
            # 'time': datetime.time(hour=16),
            # 'duration': datetime.timedelta(hours=1.5),
            'present_students': [],
            'theme': '',
            'group': groups[0]
        }
    ]

    return clients, courses, teachers, groups, lessons


def calculate_teacher_salary_for_lesson(lesson):
    return lesson['group']['course']['payment_koef'] * (len(lesson['group']['students'])) ** 0.5


def calculate_clients_payment_for_lesson(lesson):
    return lesson['group']['course']['payment_koef'] * 2 * (1 / len(lesson['group']['students']))


def input_int(question, error_message='Вы ввели не число. Попробуйте еще.', stop_words=[]):
    while True:
        number_str = input(question)  # '12'
        if number_str in stop_words:
            return number_str

        if number_str.isdigit():
            return int(number_str)
        else:
            print(error_message)


def input_link(column):
    to_list = column['to_list']  # список учителей
    main_field = column['main_field']   # фамилия

    print(f'Выберите {column["name"]}')
    n = 1
    for object in to_list:
        print(f'{n} - {object[main_field]}')
        n += 1

    number = input_int('Ваш выбор: ')
    index = number - 1

    object = to_list[index]
    return object


def input_multiple_link(column, object):  # студенты, группа
    while True:
        show_data_table('', object[column['name']], column['to_columns'])
        print(f"0 - назад\n"
              f"1 - добавить\n"
              f"2 - удалить")
        choice = input('Ваш выбор: ')
        if choice == '0':
            return
        elif choice == '1':
            not_included_objects = []
            for sub_object in column['to_list']:
                if sub_object not in object[column['name']]:
                    not_included_objects.append(sub_object)

            print('0 - назад')
            n = 1
            for sub_object in not_included_objects:
                print(f'{n} - {sub_object[column["main_field"]]}')
                n += 1

            index = input_int('Ваш выбор: ') - 1
            if index == -1:
                continue
            if 0 <= index < len(not_included_objects):
                sub_object = not_included_objects[index]
                object[column['name']].append(sub_object)
                print('Добавление успешно')
            else:
                print('Такого нету')
        elif choice == '2':
            print('0 - назад')
            n = 1
            for sub_object in object[column['name']]:
                print(f'{n} - {sub_object[column["main_field"]]}')
                n += 1

            index = input_int('Ваш выбор: ') - 1
            if index == -1:
                continue
            if 0 <= index < len(object[column['name']]):
                sub_object = object[column['name']].pop(index)
                print('Удаление успешно')
            else:
                print('Такого нету')


def input_column(column):
    if column['type'] == 'str':
        value = input(f'Введите {column["name"]}: ')
    elif column['type'] == 'int':
        value = input_int(f'Введите {column["name"]}: ')
    elif column['type'] == 'link':
        value = input_link(column)
    elif column['type'] == 'multiple_link':
        pass
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

        if column['type'] != 'multiple_link':
            value = input_column(column)
            object[column['name']] = value
        else:
            input_multiple_link(column, object)


def show_data_table(object_name, data_list, columns):
    sample = '|'
    columns_names = []
    for column in columns:
        if column['type'] != 'multiple_link':
            sample += '%-15s|'
            columns_names.append(column['name'])
    headers = sample % tuple(columns_names)
    print(headers)
    print('-' * (16 * len(columns_names) + 1))

    for dct in data_list:  # {'name': 'Bob','surname': 'Bobenko','balance': 500}
        values = []
        for column in columns:
            if column['type'] == 'multiple_link':
                pass
            elif column['type'] == 'link':
                sub_object = dct[column['name']]
                if sub_object:
                    values.append(sub_object[column['main_field']])
                else:
                    values.append('---')
            else:
                values.append(dct[column['name']])
        row_text = sample % tuple(values)
        print(row_text)
    print('-' * (16 * len(columns_names) + 1))


def work_with_objects_constructor_menu(object_name, data_list, columns, main_column_name):
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
                print(f'{n} - {object[main_column_name]}')
                n += 1

            number = int(input('Ваш выбор: '))
            index = number - 1

            object = data_list[index]
            edit_object_menu(object_name, object, columns, data_list)
        elif choice == '3':
            pass


def add_lesson(lessons, new_lesson):
    lessons.append(new_lesson)
    payment_value = calculate_clients_payment_for_lesson(new_lesson)
    for client in new_lesson['group']['students']:
        client['balance'] -= payment_value

    teacher_salary = calculate_teacher_salary_for_lesson(new_lesson)
    new_lesson['group']['teacher']['salary'] += teacher_salary


def create_new_lesson_menu(lessons, group):
    now = datetime.datetime.now()
    new_lesson = {
        'date': now.date(),
        'time': now.time(),
        'duration': datetime.timedelta(hours=1),
        'present_students': [],
        'theme': '',
        'group': group
    }
    while True:
        print('--= Редактируем урок =--\n'
              f'{new_lesson}'
              '1 - дата\n'
              '2 - time\n'
              '3 - duration\n'
              '4 - present students\n'
              '5 - theme\n'
              '6 - save\n'
              '0 - back\n')

        choice = input('Ваш выбор: ')
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            hours = float(input('Hours: '))
            new_lesson['duration'] = datetime.timedelta(hours=hours)
        elif choice == '4':
            pass
        elif choice == '5':
            new_lesson['name'] = input('New name: ')
        elif choice == '6':
            add_lesson(lessons, new_lesson)
        elif choice == '0':
            return


def check_lesson_menu(lessons, group):
    while True:
        print(f'--= Уроки группы {group["number"]} =--\n'
              f'1 - отметить новый урок\n'
              f'2 - редактировать старые уроки\n'
              f'0 - назад')
        choice = input('Ваш выбор: ')
        if choice == '0':
            return
        elif choice == '1':
            create_new_lesson_menu(lessons, group)
        elif choice == '2':
            pass


def choose_group_menu(lessons, groups):
    print('0 - back')
    n = 1
    for group in groups:
        print(f'{n} - {group["number"]} ({group["course"]["name"]})')
        n += 1

    choice = input_int('Ваш выбор:')
    if choice == 0:
        return
    index = choice - 1
    group = groups[index]
    check_lesson_menu(lessons, group)


def main_menu(clients, teachers, courses, groups, lessons):
    while True:
        print('---= Main menu =---\n'
              '1 - клиенты\n'
              '2 - учителя\n'
              '3 - курсы\n'
              '4 - группы\n'
              '5 - отметить уроки')

        choice = input('Ваш выбор: ')
        if choice == '1':
            work_with_objects_constructor_menu('client', clients, clients_columns, 'surname')
        elif choice == '2':
            work_with_objects_constructor_menu('teacher', teachers, teachers_columns, 'surname')
        elif choice == '3':
            work_with_objects_constructor_menu('course', courses, courses_columns, 'name')
        elif choice == '4':
            work_with_objects_constructor_menu('group', groups, groups_columns, 'number')
        elif choice == '5':
            choose_group_menu(lessons, groups)


def save_data(clients, courses, teachers, groups, lessons):
    data = {
        'clients': clients,
        'courses': courses,
        'teachers': teachers,
        'groups': groups,
        'lessons': lessons
    }

    with open('savings.json', 'wt', encoding='utf-8') as file:
        string = json.dumps(data, indent=4)
        file.write(string)


if __name__ == '__main__':
    clients, courses, teachers, groups, lessons = create_init_data()

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
            'name': 'payment_koef',
            'type': 'int'
        }
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
            'type': 'multiple_link',
            'to_list': courses,
            'to_columns': courses_columns,
            'main_field': 'name'
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
            'type': 'multiple_link',
            'to_list': clients,
            'to_columns': clients_columns,
            'main_field': 'surname'
        },
        {
            'name': 'teacher',
            'type': 'link',
            'to_columns': teachers_columns,
            'to_list': teachers,
            'main_field': 'surname',
        },
        {
            'name': 'course',
            'type': 'link',
            'to_columns': courses_columns,
            'to_list': courses,
            'main_field': 'name'
        },
    ]
    save_data(clients, teachers, courses, groups, lessons)
    main_menu(clients, teachers, courses, groups, lessons)
