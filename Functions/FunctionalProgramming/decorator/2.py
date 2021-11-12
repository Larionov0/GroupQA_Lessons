import time
import random


def timer(func):
    def new_func(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs)
        t_end = time.time()
        print(f"Function {func} exceeded for {t_end - t_start} s")
        return result

    return new_func


@timer
def multipler(lst, n=2):
    new_lst = []
    for number in lst:
        new_lst.append(number * n)
    return new_lst


@timer
def gen(n, min, max):
    return [random.randint(min, max) for _ in range(n)]


result = multipler([1, 2, 5, 3, 6, 32, 2, 1, 43, 34, 4, 4, 45, 46, 446, 46])
multipler(gen(1000, -100, 100))
multipler(gen(1_000_000, -1000, 1000))
multipler(gen(10_000_000, -1000, 1000))

print(result)
