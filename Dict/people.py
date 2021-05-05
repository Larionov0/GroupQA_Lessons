people = {
    'Popov': 4,
    'Aneshyn': 19,
    'Vasylyeva': 56,
    'Aleksiv': 42,
    'Pavlov': 37,
    'Babskiy': 27,
}


while True:
    print('--= Главное меню =--')
    print('1 - добавить человека')
    print('2 - просмотреть список людей')
    print('3 - удаление человека')
    print('4 - Найти фамилию человека с максимальным возрастом')

    choice = input('Ваш выбор: ')
    if choice == '1':
        surname = input('Фамилия: ')  # 'Alexich'
        age = int(input('Возраст: '))

        people[surname] = age

    elif choice == '2':
        print('Люди в базе:')
        for surname, age in people.items():
            print('Человек', surname, '- возраст:', age)

    elif choice == '3':
        surname = input('Фамилия: ')
        if surname in people:
            people.pop(surname)
            print('Удаление прошло успешно')
        else:
            print('Такого человека нету')

    elif choice == '4':
        current_max_age = 0
        current_surname = ''
        for surname, age in people.items():
            if current_max_age < age:
                current_max_age = age
                current_surname = surname
        print('Самый старший: ', current_surname, '(', current_max_age, ')')

    else:
        print(':(')
