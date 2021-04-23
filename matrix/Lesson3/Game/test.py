N = 10
M = 12


lst = [3, 3]

# создание матрицы
matrix = [['-' for _ in range(M)] for _ in range(N)]

matrix[lst[0]][lst[1]] = '+'


# вывод матрицы на экран
for row in matrix:  # [7, '3', 6, 1]
    text = '|'
    for el in row:
        text += str(el) + ' '
    print(text[:-1] + '|')

