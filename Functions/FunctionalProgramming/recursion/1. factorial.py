# 5 ! = 5 * 4 * 3 * 2 * 1 = 120
# 3 ! = 3 * 2 * 1 = 6


def norm_factorial(num):
    r = 1
    while num > 1:
        r *= num
        num -= 1
    return r


def rec_factorial(num):
    """
    f(6) = 6 * f(5)
    f(20) = 20 * f(19)

    Шаг рекурсии:
    f(n) = n * f(n - 1)

    Точка остановки:
    f(1) = 1
    """
    if num == 1:
        return 1

    return num * rec_factorial(num - 1)
