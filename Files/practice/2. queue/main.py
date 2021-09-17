SAVINGS_FILENAME = 'Data/savings.txt'


def create_init_data():
    queue = ['Вася', "Петя", "Алина"]
    count = 0
    name = 'Отель Жож'
    return queue, count, name


def add_guest_menu(queue):
    name = input('Имя: ')
    queue.append(name)


def main_menu(queue, count, name):
    while True:
        print(f'--= Меню очереди {name} =--\n'
              f'{queue}\n'
              f'Обработано: {count}\n'
              '1 - добавить гостя\n'
              '2 - гость обработан\n'
              '3 - изменить имя\n'
              '4 - сохранить\n'
              '0 - выход')
        choice = input('Your choice: ')
        if choice == '1':
            add_guest_menu(queue)
        elif choice == '2':
            if queue:
                queue.pop(0)
                count += 1
        elif choice == '3':
            name = input('Новое имя: ')
        elif choice == '4':
            save_data(queue, count, name)
            print('Данные сохранены')
        elif choice == '0':
            save_data(queue, count, name)
            break


def save_data(queue, count, name):
    with open(SAVINGS_FILENAME, 'wt', encoding='utf-8') as file:
        file.write(f"{name}\n{count}\n{','.join(queue)}")


def load_data():
    with open(SAVINGS_FILENAME, 'rt', encoding='utf-8') as file:
        name = file.readline().rstrip()
        count = int(file.readline())
        queue = file.readline().rstrip().split(',')
    return queue, count, name


def try_to_load_data():
    try:
        return load_data()
    except Exception as exc:
        print(f'Произошла ошибка при загрузке вашего сохранения:\n{exc}')
        return create_init_data()


queue, count, name = try_to_load_data()
main_menu(queue, count, name)
