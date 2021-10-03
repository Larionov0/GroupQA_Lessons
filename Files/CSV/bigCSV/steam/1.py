import plotly.graph_objs as go


def bubble_sort_cut(numbers, second_list, n):
    length = len(numbers)

    ogr = length - 1
    while ogr >= length - n:
        i = 0
        while i < ogr:
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                second_list[i], second_list[i + 1] = second_list[i + 1], second_list[i]
            i += 1
        ogr -= 1
    return numbers[length - n:], second_list[length - n:]


def compare_developers_by_games_amount(filename='steam.csv'):
    """
    Написать функцию, которая построит круговой график с
    разработчиками и количеством выпущенных продуктов каждого из них.
    """
    counts = {}
    with open('steam.csv', 'rt', encoding='utf-8') as file:
        headers = file.readline().rstrip().split(',')
        dev_index = headers.index('developer')

        line_n = 1
        for line in file:
            developer = line.rstrip().split(',')[dev_index]

            if developer not in counts:
                counts[developer] = 0
            counts[developer] += 1

            if line_n % 1000 == 0:
                print(f"Обработано: {line_n}")
            line_n += 1

    devs = list(counts.keys())
    counts = list(counts.values())

    sorted_top_counts, sorted_top_devs = bubble_sort_cut(counts, devs, 30)

    diag = go.Pie(labels=sorted_top_devs, values=sorted_top_counts)
    go.Figure(data=[diag]).show()


compare_developers_by_games_amount()
