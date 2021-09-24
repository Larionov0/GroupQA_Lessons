SAVING_FILENAME = 'Data/saving.txt'


def create_init_data():
    storage_type = 'money box'
    expenses = ['купил мясо']
    income = ['украл']
    money = 0
    return storage_type, money, expenses, income


def main_menu(storage_type, money, expenses, income):
    while True:
        print(f'\n***My {storage_type} : {money}***\n'
              f'Доходы с : {", ".join(income)}\n'
              f'Расходы на: {", ".join(expenses)}\n\n'
              '1 - Редактор доходов\n'
              '2 - Редактор расходов\n'
              '3 - Сохранить\n'
              '0 - Выход')
        choice = input('\nYour choice: ')
        if choice == '1':
            print('\n--Доходы--\n')
            print('1 - Добавить доходы \n'
                  '2 - Очистить список доходов\n')
            choice_income = input('\nYour choice in income: ')
            if choice_income == '1':
                money += int(input('Добавить денег: '))
                income.append(input('За какую работу: '))
            elif choice_income == '2':
                income.clear()

        elif choice == '2':
            print('\n--Расходы--\n')
            print('1 - Добавить расходы \n'
                  '2 - Очистить список расходов\n')
            choice_expenses = input('\nYour choice in income: ')
            if choice_expenses == '1':
                money -= int(input('Потратить денег: '))
                expenses.append(input('На что: '))
            elif choice_expenses == '2':
                expenses.clear()

        elif choice == '3':
            save_data(storage_type, money, expenses, income)
            print('Данные сохранены')
        elif choice == '0':
            save_data(storage_type, money, expenses, income)
            break


def save_data(storage_type, money, expenses, income):
    with open(SAVING_FILENAME, 'wt', encoding='utf-8') as file:
        file.write(f"{storage_type}\n{money}\n{','.join(expenses)}\n{','.join(income)}")


def load_data():
    with open(SAVING_FILENAME, 'rt', encoding='utf-8') as file:
        storage_type = file.readline().rstrip()
        money = int(file.readline())
        expenses = file.readline().rstrip().split(',')
        income = file.readline().rstrip().split(',')
    return storage_type, money, expenses, income


def try_to_load_data():
    try:
        return load_data()
    except Exception as exc:
        print(f'Произошла ошибка при загрузке вашего сохранения:\n{exc}')
        return create_init_data()


storage_type, money, expenses, income = try_to_load_data()
main_menu(storage_type, money, expenses, income)
