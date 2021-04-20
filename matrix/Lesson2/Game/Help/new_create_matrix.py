N = 3
M = 5


# создание матрицы
matrix = [['-' for _ in range(M)] for _ in range(N)]

# вывод матрицы на экран
for row in matrix:  # [7, '3', 6, 1]
    text = '|'
    for el in row:
        text += str(el) + ' '
    print(text[:-1] + '|')
