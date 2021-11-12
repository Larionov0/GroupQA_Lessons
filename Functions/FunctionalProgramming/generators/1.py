def my_range(start, stop, step=1):
    lst = []
    while start < stop:
        lst.append(start)
        start += step
    return lst


def my_gen_range(start, stop, step=1):
    while start < stop:
        yield start
        start += step


for i in my_gen_range(0, 10):
    print(i)
