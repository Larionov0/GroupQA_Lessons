def sum_of_digits(num):
    """
    Шаг рекурсии:
    f(1945) = 5 + f(194)
    f(194) = 4 + f(19)
    f(19) = 9 + f(1)
    f(1) = 1 + f(0)

    ! точка остановки
    f(0) = 0
    """
    if num == 0:
        return 0

    last_digit = num % 10
    number = num // 10
    return last_digit + sum_of_digits(number)


def sum_of_digits_with_state(num, sum_=0):
    if num == 0:
        return sum_

    last_digit = num % 10
    number = num // 10

    return sum_of_digits_with_state(number, sum_ + last_digit)


print(sum_of_digits_with_state(190455))
