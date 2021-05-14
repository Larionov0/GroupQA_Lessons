N = 5
M = 6

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


# print(matrix)
for row in matrix:  # [7, '3', 6, 1]
    text = '|'
    for el in row:
        text += str(el) + ' '
    print(text[:-1] + '|')
