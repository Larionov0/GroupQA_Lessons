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


def task3(filename, result_filename):
    """
    Нужно подсчитать количество овощей каждого типа, и
    записать в новый csv - файл с колонками:
    овощ, вес, сорта
    помидор, 45, 0;1
    ....
    """
    with open(filename, 'rt', encoding='utf-8') as file:
        headers = file.readline().rstrip().split(', ')
        name_index = headers.index('название')
        m_index = headers.index('масса')
        sort_index = headers.index('сорт')

        vegs = {
            # 'помидор': {
            #     'm': 45,
            #     'sorts': [1, 2]
            # },
            # 'чеснок': {
            #     'm': 45,
            #     'sorts': [1, 2]
            # }
        }

        for line in file:  # '1, помидор, 15, 12.05.2021, ящик, 3, 0'
            line_list = line.rstrip().split(', ')

            name = line_list[name_index]  # 'помидор'
            m = int(line_list[m_index])  # 15
            sort = int(line_list[sort_index])  # 0

            if name in vegs:
                veg_dict = vegs[name]
                veg_dict['m'] += m
                if sort not in veg_dict['sorts']:
                    veg_dict['sorts'].append(sort)
            else:
                vegs[name] = {
                    'm': m,
                    'sorts': [sort]
                }

        with open(result_filename, 'wt', encoding='utf-8') as file:
            headers = ['название', "масса", "сорта"]
            file.write(', '.join(headers) + "\n")

            for name, veg_dict in vegs.items():
                sorts = [str(int_sort) for int_sort in veg_dict['sorts']]
                file.write(f"{name}, {veg_dict['m']}, {';'.join(sorts)}\n")


task3('vegs.csv', 'result.csv')
