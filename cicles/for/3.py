numbers = []
n = 0
i = 0
print('как утсали введите - стоп')
while i <= len(numbers):
    number = input('введите овощ:   ')
    if number == 'стоп':
        break
    numbers.append(number)
    i += 1

print(numbers)

v = input('Введите букву:  ')
i = 0
for n in numbers:
    if v in n:
        print(i)
    i += 1
