mat = [
    [4, 1, 3, 67, 0],
    [50, 23, 6, 4, 2],
    [88, 89, 4, 1, 1],
    [3, 0, 6, 33, 44]
]

while True:
    num = int(input("Введите номер ряда: "))
    if num > len(mat):
        print("Введите число меньше ", len(mat))
    else:
        i = 0
        while i < len(mat[num]):
            mat[num][i] = float('inf')
            i += 1
        print(mat)


