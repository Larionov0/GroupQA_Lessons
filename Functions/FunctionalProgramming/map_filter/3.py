input_str = input('Input numbers with "+" separator: ')  # '2+4+1+5+3'

numbers = input_str.split('+')  # ['2', '1', '5', '4']
numbers = map(int, numbers)
# numbers = [int(number) for number in numbers]
print(sum(numbers))


# print(sum(map(int, input('Input numbers with "+" separator: ').split('+'))))  - вариант этой же программы в одну строку
