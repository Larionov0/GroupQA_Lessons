N = 14
M = 16

hero_coords = [2, 3]
hero_name = 'Bob'
hero_hp = 10
hero_sprite = '+'

while True:
    # создание матрицы
    matrix = [['-' for _ in range(M)] for _ in range(N)]

    # отрисовываем героя на матрице
    matrix[hero_coords[0]][hero_coords[1]] = hero_sprite

    # вывод матрицы на экран
    for row in matrix:  # [7, '3', 6, 1]
        text = '|'
        for el in row:
            text += str(el) + ' '
        print(text[:-1] + '|')

    choice = input('WASD: ')

    if choice == 'w':
        hero_coords[0] -= 1
    elif choice == 'a':
        hero_coords[1] -= 1
    elif choice == 's':
        hero_coords[0] += 1
    elif choice == 'd':
        hero_coords[1] += 1
