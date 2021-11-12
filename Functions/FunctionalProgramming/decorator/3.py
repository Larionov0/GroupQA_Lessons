def printer_decor_creator(n=30):
    def printer_decorator(func):
        def new_func(*args, **kwargs):
            print('-' * n)
            func(*args, **kwargs)
            print('-' * n)
        return new_func
    return printer_decorator


@printer_decor_creator(15)
def helloer(name):
    print(f'Hello, {name}! :)')


@printer_decor_creator()
def print_list(lst):
    for el in lst:
        print(f'- {el}')


@printer_decor_creator(100)
def print_triangle(n):
    for a in range(1, n + 1):
        print("*" * a)


@printer_decor_creator()
def print_matrix(matrix):
    text = ''
    for row in matrix:
        text += '|'
        for el in row:
            text += str(el) + ' '
        text = text[:-1] + '|\n'
    print(text)


@printer_decor_creator(1)
def hello_world():
    print('Hello world!')


@printer_decor_creator()
def love(name1, name2):
    print(f'{name1} + {name2} = LOVE')


hello_world()
print_triangle(100)
