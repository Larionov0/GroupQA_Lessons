def upak_count(filename, needed_upak):
    """
    :param upak: тип упаковки
    :return: количество задействованых упаковок такого типа на складе
    """
    with open(filename, 'rt', encoding='utf-8') as file:
        file.readline()
        total_count = 0
        for line in file:  # "1, помидор, 15, 12.05.2021, ящик, 3, 0\n"
            veg_data = line.rstrip().split(', ')
            upak = veg_data[4]
            if upak == needed_upak:
                total_count += int(veg_data[5])
    return total_count


# print(upak_count('vegs.csv', 'asfasf'))

def find_max_veg(filename):
    vegs_ms = {}
    with open(filename, 'rt', encoding='utf-8') as file:
        file.readline()
        for line in file:
            line_data = line.rstrip().split(', ')
            name = line_data[1]
            m = int(line_data[2])
            if name not in vegs_ms:
                vegs_ms[name] = 0
            vegs_ms[name] += m

    max_veg = []
    max_count = 0
    for veg, m in vegs_ms.items():
        if m > max_count:
            max_count = m
            max_veg.clear()
            max_veg.append(veg)
        elif m == max_count:
            max_veg.append(veg)

    return max_veg, max_count


print(find_max_veg('vegs.csv'))
