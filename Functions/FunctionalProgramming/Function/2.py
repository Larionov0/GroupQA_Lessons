def adder(a, b):
    return a + b


def minus(a, b):
    return a - b


lst = [adder, minus, print]


lst[2]('Hello')
