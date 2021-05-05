import random
from os import system


N = 16
M = 20


hero_name = 'Bobby'
hero_hp = 10
hero_coords = [3, 4]
hero_sprite = '+'
hero_details = 0


animals = [
    ['kurka', 'Ryaba', 3, [5, 5], 'k'],
    ['kurka', 'Biba', 3, [6, 5], 'k'],
    ['kurka', 'Marusya', 3, [5, 6], 'k'],
]


round_ = 1
while True:
    # создание матрицы
    matrix = [['-' for _ in range(M)] for _ in range(N)]

    # прорисовка обьектов
    # рисуем героя
    matrix[hero_coords[0]][hero_coords[1]] = hero_sprite

    # рисуем животных
    for animal in animals:  # ['kurka', 'Ryaba', 3, [5, 6], 'k']
        animal_coords = animal[3]  # [5, 6]
        animal_sprite = animal[-1]
        matrix[animal_coords[0]][animal_coords[1]] = animal_sprite

    system('cls')
    # вывод матрицы на экран
    for row in matrix:  # [7, '3', 6, 1]
        text = '|'
        for el in row:
            text += str(el) + ' '
        print(text[:-1] + '|')

    print(hero_coords)

    # все ходят
    # герой делает ход
    print("Герой", hero_name)
    print("Детали:", hero_details)
    print('wasd - ходить')
    step = int(input('Кол-во шагов:  '))
    choice = input('Ваш выбор: ')


    if choice == 'w':
        if hero_coords[0] != 0:
            hero_coords[0] -= 1*step
    elif choice == 'a':
        if hero_coords[1] == 0:
            hero_coords[1] = M - 1
        else:
            hero_coords[1] -= 1*step
    elif choice == 's':
        if hero_coords[0] != N - 1:
            hero_coords[0] += 1*step
    elif choice == 'd':
        if hero_coords[1] == M - 1:
            hero_coords[1] = 0
        else:
            hero_coords[1] += 1*step
    else:
        print('Такого варианта нету :(')

    # не поймал ли курицу
    caught_kurkas = []

    for animal in animals:
        if animal[0] == 'kurka' and animal[3] == hero_coords:
            hero_details += 3
            caught_kurkas.append(animal)

    for kurka in caught_kurkas:
        animals.remove(kurka)

    # животные делают ход
    for animal in animals:  # ['kurka', 'Ryaba', 3, [5, 6], 'k']
        if animal[0] == 'kurka':
            direction = random.choice(['w', 'a', 's', 'd'])
            kurka_coords = animal[3]

            if direction == 'w':
                if kurka_coords[0] != 0:
                    kurka_coords[0] -= 1
            elif direction == 'a':
                if kurka_coords[1] == 0:
                    kurka_coords[1] = M - 1
                else:
                    kurka_coords[1] -= 1
            elif direction == 's':
                if kurka_coords[0] != N - 1:
                    kurka_coords[0] += 1
            elif direction == 'd':
                if kurka_coords[1] == M - 1:
                    kurka_coords[1] = 0
                else:
                    kurka_coords[1] += 1

        elif animal[0] == 'olen':
            pass

    # не поймал ли курицу
    caught_kurkas = []

    for animal in animals:
        if animal[0] == 'kurka' and animal[3] == hero_coords:
            hero_details += 3
            caught_kurkas.append(animal)

    for kurka in caught_kurkas:
        animals.remove(kurka)

    # появление животных
    if round_ % 15 == 0:  # появление курицы
        name = random.choice(['Ryaba', 'Boba', 'Biba', 'Byba', 'Misha', 'Klava'])
        new_kurka = ['kurka', name, 3, [random.randint(0, N - 1), random.randint(0, M - 1)], 'k']
        animals.append(new_kurka)
    if round_ % 40 == 0:  # появление оленя
        pass

    round_ += 1
