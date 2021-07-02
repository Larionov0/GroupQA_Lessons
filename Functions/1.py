import random


def helloer():
    print('Здравствуйте!')


def print_line(dashes_amount):
    print('-' * dashes_amount)


def helloer2(name):
    print(f'Привет, {name}')


def find_average_from_3(a, b, c):
    return (a + b + c) / 3

# n1 = int(input('Оценка1: '))
# n2 = int(input('Оценка2: '))
# n3 = int(input('Оценка3: '))
#
# r = find_average_from_3(n1, n2, n3)
# print(r)
# if 10 <= r <= 12:
#     print('Отличник')
# elif r >= 7:
#     print('Хорошист')
# elif r >= 4:
#     print('Троечник')
# else:
#     print('Двоечник')


def calc_distance(x1, y1, x2, y2):
    result = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return result


# Пользователь вводит координаты круга и радиус
# Затем пользователь вводит координаты точек.
# Вывести все точки, которые попадают в круг
# r = int(input('Радиус круга: '))
# cir_x = int(input('Координата х круга: '))
# cir_y = int(input('Координата y круга: '))
#
# points = []
# while True:
#     x = input('X: ')
#     if x == 'stop':
#         break
#     x = int(x)
#     y = int(input('Y: '))
#     point = [x, y]
#     points.append(point)
#
#
# print('Точки внутри круга: ')
# for point in points:
#     d = calc_distance(point[0], point[1], cir_x, cir_y)
#     if d <= r:
#         print(point, d)

def input_int(question, error_message='Вы ввели не число. Попробуйте еще.', stop_words=[]):
    while True:
        number_str = input(question)  # '12'
        if number_str in stop_words:
            return number_str

        if number_str.isdigit():
            return int(number_str)
        else:
            print(error_message)


# age = input_int('Введите возраст: ', 'Возраст числовой!')
# print(age + 1)
#
# number = input_int("Число: ")
# print(number * 10)

def input_numbers_list(question, input_question='Введите число ', stop_words=['stop', 'стоп'], numeration=False):
    print(question)
    numbers = []
    numer = 1
    while True:
        if numeration:
            number = input_int(f'{input_question} №{numer}: ', stop_words=stop_words)
        else:
            number = input_int(f'{input_question}: ', stop_words=stop_words)
        if number in stop_words:
            break
        else:
            numbers.append(number)
        numer += 1
    return numbers


def calc_average(numbers):
    return sum(numbers) / len(numbers)


# numbers = input_numbers_list('Введите числа для суммы', stop_words=['астанавитязь', "а"])
# print("Сумма =", sum(numbers))
#
#
# marks = input_numbers_list('Вводите оценки по очереди: ', 'Введите что-то ', numeration=True)
# print('Средний балл: ', calc_average(marks))


def print_matrix(matrix):
    for row in matrix:  # [7, '3', 6, 1]
        text = '|'
        for el in row:
            text += str(el) + ' '
        print(text[:-1] + '|')


def create_matrix(n, m, filler='-'):
    matrix = []

    for _ in range(n):
        row = []
        for _ in range(m):
            if filler == 'random':
                row.append(random.randint(0, 9))
            else:
                row.append(filler)
        matrix.append(row)
    return matrix


matrix1 = create_matrix(4, 6)
print_matrix(matrix1)


matrix2 = create_matrix(10, 20, 'random')
print_matrix(matrix2)
