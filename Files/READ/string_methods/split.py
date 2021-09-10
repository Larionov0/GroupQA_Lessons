string = input('Вводите числа разделяя их +: ')

numbers = string.split('+')  # разбивает строку по разделителю, возвращает список подстрок

sum_ = 0
for number in numbers:
    sum_ += int(number)

# sum_ = sum([int(number) for number in numbers])

print(sum_)
