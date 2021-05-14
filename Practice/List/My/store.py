products = [
    ['хлеб', 12, 34, 1],
    ['булка', 20, 15, 1],
    ['стейк свинной', 140, 5, 2],
    ['крылья коровы', 410, 3, 2],
    ['сырный соус', 30, 6, 3],
    ['сыр Чеддер', 120, 4, 4],
    ['сыр Пармезан', 300, 5, 4]
]

proizvoditeli = [
    [1, 'Херсонская Хлебоварня', ['Киев', "Одесса", "Херсон"], 6],
    [2, 'Мясокомбинат Свинка', ['Киев', "Харьков"], 3],
    [3, 'Соусная "Безнадёга"', ["Чернигов"], 9],
    [4, 'Сыроварня "Носок"', ['Киев', "Херсон", "Чернигов", "Черновцы"], 7]
]


while True:
    print('\n\n--= Главное меню =--\n'
          '1 - создать товар\n'
          '2 - удалить товар\n'
          '3 - найти самый дешевый товар\n'
          '4 - подсчитать, на какую сумму товары на складе\n'
          '5 - все товары\n'
          '6 - редактирование товара')
    choice = input('Ваш выбор: ')
    if choice == '1':
        pass
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        print('Все продукты:\n')
        print('Имя | Стоимость | Количество | Производитель')
        for product in products:
            print(product[0], "|", product[1], "|", product[2], '|', product[3])
        print('-' * 40)
    elif choice == '6':
        print('\n\nВыберите продукт:')
        print('0 - отбой')
        i = 1
        for product in products:
            print(i, '-', product[0])
            i += 1
        choice = int(input('Выберите товар: '))
        if 0 < choice < len(products):
            product = products[choice - 1]
            while True:
                print("\n\n--= Меню редактирования товара =--")
                print('Товар ', product[0])
                print(product[1], 'грн; Количество:', product[2])
                print('Производитель: ', product[3])
                print('--------------------')
                print("1 - изменить имя\n"
                      "2 - изменить стоимость\n"
                      "3 - изменить количество\n"
                      "4 - изменить производителя\n"
                      "5 - назад в главное меню")
                choice = input('Ваш выбор: ')
                if choice == '1':
                    new_name = input('Введите новое имя: ')
                    if len(new_name) < 3:
                        print('Мало буков')
                    else:
                        product[0] = new_name

                elif choice == '2':
                    price = float(input('Новая стоимость: '))
                    if price <= 0:
                        print('Маловато')
                    else:
                        product[1] = price

                elif choice == '3':
                    amount = float(input('Новое количество: '))
                    if price <= 0:
                        print('Маловато')
                    else:
                        product[2] = amount

                elif choice == '4':
                    pass

                elif choice == '5':
                    break

    elif choice == '6':
        pass
    else:
        pass
