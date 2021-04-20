matrix = [
    [4, 1, 3, 67, 0, 3, 2],
    [50, 23, 6, 4, 2, 6, 3],
    [88, 89, 4, 1, 1, 8, 4],
    [3, 0, 6, 33, 44, 1, 7]
]

# # вывод 0 ряда
# print(matrix[0][0])
# print(matrix[0][1])
# print(matrix[0][2])
# print(matrix[0][3])
# print(matrix[0][4])
# print(matrix[0][5])
# print(matrix[0][6])
#
# # вывод 1 ряда
# print(matrix[1][0])
# print(matrix[1][1])
# print(matrix[1][2])
# print(matrix[1][3])
# print(matrix[1][4])
# print(matrix[1][5])
# print(matrix[1][6])
#
# # вывод 2 ряда
# print(matrix[2][0])
# print(matrix[2][1])
# print(matrix[2][2])
# print(matrix[2][3])
# print(matrix[2][4])
# print(matrix[2][5])
# print(matrix[2][6])
#
# # вывод 3 ряда
# print(matrix[3][0])
# print(matrix[3][1])
# print(matrix[3][2])
# print(matrix[3][3])
# print(matrix[3][4])
# print(matrix[3][5])
# print(matrix[3][6])


i = 0
while i < len(matrix):
    j = 0
    while j < len(matrix[0]):
        print(matrix[i][j])
        j += 1
    print('------')
    i += 1

