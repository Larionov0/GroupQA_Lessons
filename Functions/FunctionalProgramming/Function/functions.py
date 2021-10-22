def adder(a, b):
    return a + b


a = adder

print(a(1, 2))
print(adder(1, 2))

print(a is adder)
