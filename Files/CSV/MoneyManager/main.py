import datetime

FILE = 'records.csv'


def edit_record_menu(record, data):
    while True:
        print('---| Редактирование записи доходов/расходов |---\n\n'
              f'{record}\n'
              f'1 - сумма\n'
              f'2 - текст\n'
              f'3 - дата\n'
              f'4 - удалить\n'
              f'0 - сохранить и выйти')
        choice = input('Ваш выбор: ')

        if choice == '1':
            record['sum'] = int(input('Сума: '))
        elif choice == '2':
            record['text'] = input('Текст: ')
        elif choice == '3':
            pass
        elif choice == '4':
            data['records'].remove(record)
            print('Удалено')
        elif choice == '0':
            return


def create_init_data():
    data = {
        'name': 'Bob',
        'records': [
            {
                'text': 'Купил сосиску в тесте',
                'sum': -20,
                'date': datetime.datetime(year=2021, month=9, day=24)
            },
            {
                'text': 'Получил зп',
                'sum': 12000,
                'date': datetime.datetime(year=2021, month=9, day=20)
            },
        ]
    }
    return data


def records_menu(data):
    while True:
        print('--= Доходы/расходы =--\n'
              f'Текущая сума: {sum([record["sum"] for record in data["records"]])}\n'
              f'Последние записи:')
        for record in data['records']:
            print('- ', record)
        print('1 - добавить запись\n'
              '2 - редактировать\n'
              '0 - назад'
              )
        choice = input('Ваш выбор: ')
        if choice == '1':
            record = {
                'text': 'Новая запись',
                'sum': 0,
                'date': datetime.datetime.now()
            }
            data['records'].append(record)
            edit_record_menu(record, data)

        elif choice == '2':
            pass
        elif choice == '0':
            return


def main_menu(data):
    while True:
        print('--= Главное меню =--\n'
              '1 - доходы/расходы\n'
              '2 - статистика\n'
              '3 - сохранение\n'
              '4 - выход'
              )
        choice = input('Ваш выбор: ')
        if choice == '1':
            records_menu(data)
        elif choice == '2':
            pass
        elif choice == '3':
            save_data(data)
        elif choice == '4':
            return


def save_data(data):
    with open(FILE, 'wt', encoding='utf-8') as file:
        file.write('text, sum, date\n')
        for record in data['records']:
            file.write(f"{record['text']}, {record['sum']}, {record['date']}\n")


def load_data():
    with open(FILE, 'rt', encoding='utf-8') as file:
        headers = file.readline()
        records = []
        for line in file:
            line_list = line.rstrip().split(', ')
            dct = {
                'text': line_list[0],
                'sum': int(line_list[1]),
                'date': datetime.datetime.fromisoformat(line_list[2])
            }
            records.append(dct)

    return {
        'name': "Bob",
        'records': records
    }


def try_to_load_data():
    try:
        return load_data()
    except Exception as exc:
        print(f'Произошла ошибка при загрузке вашего сохранения:\n{exc}')
        return create_init_data()


data = try_to_load_data()
main_menu(data)
