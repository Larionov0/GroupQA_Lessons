# Пользователь вводит 7 имен.
# Вывести количество больших имен, средних и маленьких
# большие, если >= 8 букв
# средние, если 5 <= и < 8
# маленькие, если <= 4 букв

print('Вводите имена с маленькой буквы')
n1 = input('Name 1: ')
n2 = input('Name 2: ')
n3 = input('Name 3: ')
n4 = input('Name 4: ')
n5 = input('Name 5: ')
n6 = input('Name 6: ')
n7 = input('Name 7: ')


count_s = 0
count_m = 0
count_l = 0

if len(n1) <= 4:
    count_s += 1
elif len(n1) < 8:
    count_m += 1
else:
    count_l += 1

if len(n2) <= 4:
    count_s += 1
elif len(n2) < 8:
    count_m += 1
else:
    count_l += 1

if len(n3) <= 4:
    count_s += 1
elif len(n3) < 8:
    count_m += 1
else:
    count_l += 1

if len(n4) <= 4:
    count_s += 1
elif len(n4) < 8:
    count_m += 1
else:
    count_l += 1

if len(n5) <= 4:
    count_s += 1
elif len(n5) < 8:
    count_m += 1
else:
    count_l += 1

if len(n6) <= 4:
    count_s += 1
elif len(n6) < 8:
    count_m += 1
else:
    count_l += 1

if len(n7) <= 4:
    count_s += 1
elif len(n7) < 8:
    count_m += 1
else:
    count_l += 1


print('Маленьких имен: ' + str(count_s))
print('Средних имен: ' + str(count_m))
print('Больших имен: ' + str(count_l))
