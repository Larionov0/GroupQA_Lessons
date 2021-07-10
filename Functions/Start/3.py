def center(string):
    if len(string) % 2 == 0:  # четное
        return string[len(string) // 2 - 1] + string[len(string) // 2]
    else:  # нечетное
        return string[len(string) // 2]


a = center('abcdef')

print(a)
