print(':)')
try:
    2 / 0
except ValueError:
    print('Что-то не так')
except ZeroDivisionError:
    print('Деление на ноль')
print(':(')
