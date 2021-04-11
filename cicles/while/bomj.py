import random
import time


money = 50
things = ['штаны', "шапка"]
satiety = 10
can_work_math = True

products_names =  ['тапки', 'хлеб', 'футболка', 'спорт костюм', 'телефон', 'смартфон', 'квартира']
products_prices = [40,      10,     100,         150,            200,       1000,       100000]

print('Вы жили себе мирной жизнью, но однажды')
print('вы выпали из окна, не взяв ключи.')
print('Теперь вы бездомный. Ваша задача - накопить на новую квартиру.')

while True:
    print('\n\n\n--= Главное меню =--')
    print('Деньги: ' + str(money))
    print('Вещи: ' + str(things))
    print('1 - в магазин')
    print('2 - на заработки')
    print('3 - подраться с другим бомжом за территорию')
    print('4 - порыться на свалке')
    print('5 - выход из игры')

    choice = input('Ваш выбор: ')
    if choice == '1':
        while True:
            print('\n\n--= Магазин =--')
            print('Деньги: ' + str(money))
            print('Вещи: ' + str(things))
            print('0 - назад')

            i = 0
            while i < len(products_names):
                print(str(i + 1) + ' - ' + products_names[i] + ' (' + str(products_prices[i]) + ' грн)')
                i += 1

            choice = input('Ваш выбор: ')
            if choice == '0':
                break

            index = int(choice) - 1
            if 0 <= index < len(products_names):
                price = products_prices[index]
                product_name = products_names[index]
                
                if money >= price:
                    money -= price
                    things.append(product_name)
                    print('Покупка успешна!')
                else:
                    print('Недостаточно денег!')
            else:
                print('Такого варианта нету')          
        
    elif choice == '2':
        while True:
            print('\n\n--= Заработки =--')
            print('Деньги: ' + str(money))
            print('Вещи: ' + str(things))
            print('0 - назад')
            print('1 - попрошайничать (3 - 20 грн)')
            print('2 - собирать бутылки (6 - 14 грн)')
            print('3 - работать гружчиком (40 грн) (нужны тапки)')
            print('4 - устроиться курьером (70 грн) (нужны тапки, спорт костюм)')
            print('5 - работать менеджер (200 грн, если клиент согласиться) (нужен телефон, футболка)')
            print('6 - работать математиком (400 грн при успехе) (нужен телефон, костюм)')
            choice = input('Ваш выбор: ')

            if choice == '0':
                break
            elif choice == '1':
                print('Бомж попрошайничает...')
                time.sleep(3)
                zar = random.randint(3, 20)
                money += zar
                print('Вы заработали ' + str(zar) + ' грн')
                
            elif choice == '2':
                print('Бомж собирает бутылки...')
                time.sleep(random.randint(1, 5))
                zar = random.randint(6, 14)
                money += zar
                print('Вы заработали ' + str(zar) + ' грн')
                
            elif choice == '3':
                if 'тапки' in things:
                    input('Бомж таскает мешки')
                    input('Перетаскивает ящики')
                    input('Идет в Верховную Раду')
                    input('Разгружает фуры')
                    print('Осталось только почистить обувь начальнику...')
                    time.sleep(2)
                    zar = 40
                    money += zar
                    print('Вы заработали ' + str(zar) + ' грн')
                else:
                    print('Недостаточно вещей!')

            elif choice == '6':
                if can_work_math == True:
                    if 'телефон' in things and 'костюм' in things:
                        n1 = random.randint(1, 100)
                        n2 = random.randint(1, 100)
                        answer = int(input(str(n1) + ' + ' + str(n2) + ' = '))
                        if n1 + n2 == answer:
                            zar = 400
                            money += zar
                            print('Вы заработали ' + str(zar) + ' грн')
                        else:
                            print('Вы уволены! Не возвращайтесь.')
                            can_work_math = False
                    else:
                        print('Недостаточно вещей!')
                else:
                    print('Вы же уволены!')
        
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        break
    else:
        pass
