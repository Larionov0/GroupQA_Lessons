names = ["Alice", "Petya", "Lesha:"]

while True:
    print(" Меню списка")
    print(" 1 - войти в очередь")
    print("2 - покинуть очередь")
    print('3 - вывести на экран')
    
    choice = input(" Ваш выбор")
    if choice == "2":
        if len(names) > 0:
            name = names.pop (0)
            print(name)
            if len(names)== 0:
                print("Список пуст")
        else:
            print('Очередь уже пуста')
    elif choice == "1":
        name= input ("Введите имя: ")
        names.append(name)

    elif choice == '3':
        print(names)
