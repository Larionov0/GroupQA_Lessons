def f(*numbers, **kwargs):
    print(kwargs)
    print(kwargs['a'])
    print(kwargs.keys())
    s = 0
    for number in numbers:
        s += number
    return s


print(f(4, 5, 6, 2, 4, a=2, test='lol', kek='bob'))
