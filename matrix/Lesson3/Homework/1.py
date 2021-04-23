matrix = [
    [47, 11, 39, 67, 10],
    [50, 23, 65, 48, 22],
    [88, 89, 44, 12, 19],
    [35, 30, 66, 33, 44]
]
print(matrix)
a = int(input('Enter number:  '))
i = 0
while i < len(matrix):
    j = 0
    while j < len(matrix[0]):
        if a == matrix[i][j]:
            print(str(i) + ' ' + 'строка' + '-', str(j) + ' ' + 'столбец')
        j += 1
    i += 1
