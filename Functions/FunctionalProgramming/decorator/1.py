def printer_decorator(func):
    def new_func(*args, **kwargs):
        print('-' * 30)
        func(*args, **kwargs)
        print('-' * 30)
    return new_func


@printer_decorator
def helloer(name):
    print(f'Hello, {name}! :)')


@printer_decorator
def print_list(lst):
    for el in lst:
        print(f'- {el}')


@printer_decorator
def print_triangle(n):
    for a in range(1, n + 1):
        print("*" * a)


@printer_decorator
def print_matrix(matrix):
    text = ''
    for row in matrix:
        text += '|'
        for el in row:
            text += str(el) + ' '
        text = text[:-1] + '|\n'
    print(text)


@printer_decorator
def hello_world():
    print('Hello world!')


@printer_decorator
def love(name1, name2):
    print(f'{name1} + {name2} = LOVE')


love('Anna', name2='Vasya')
hello_world()
