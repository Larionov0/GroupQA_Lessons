"""
Задача: написать функцию, которая вернет список слов из файла words.txt
"""


def read_words(filename):
    file = open(filename, 'rt', encoding='utf-8')

    result_words = []
    for line in file:
        line = line.rstrip()  # 'плюшка, пельмень, диск'
        words = line.split(',')  # ['плюшка', 'пельмень', 'диск']

        for word in words:
            result_words.append(word.strip())

    file.close()
    return result_words


print(read_words('words.txt'))
