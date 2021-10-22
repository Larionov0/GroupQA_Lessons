def x2(num):
    return num * 2


numbers = [1, 5, 3, 7, 43, 7, 3, 45, 34]


result = list(map(x2, numbers))
print(result)
