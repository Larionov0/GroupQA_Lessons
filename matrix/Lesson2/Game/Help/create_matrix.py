N = 100
M = 200


# создание матрицы
matrix = []
i = 0
while i < N:
    row = []
    j = 0
    while j < M:
        row.append('-')
        j += 1
    matrix.append(row)
    i += 1


# вывод матрицы на экран
for row in matrix:  # [7, '3', 6, 1]
    text = '|'
    for el in row:
        text += str(el) + ' '
    print(text[:-1] + '|')
