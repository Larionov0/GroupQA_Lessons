mat = [
    [4, 1, 3, 67, 0],
    [50, 23, 6, 4, 2],
    [88, 89, 4, 1, 1],
    [3, 0, 6, 33, 44]
]
i = 0
p = 0

i = int(input("Введите номер ряда: "))
j = 0
for symb in mat[i]:
    mat[i][j] = float('inf')
    j += 1

print(mat)
