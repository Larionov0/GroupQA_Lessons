"""
Пользователь вводит номер столбца.
Программа должна вывести все элементы столбца.
Каждый в новой строке.
"""

matrix = [
    [1, 5, 3, 6],
    [7, 3, 6, 1],
    [4, 7, 8, 5]
]

j = int(input('Номер столбца: '))  # 2

i = 0
while i < len(matrix):
    print(matrix[i][j])
    i += 1
