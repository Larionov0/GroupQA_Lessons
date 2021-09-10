file = open('test.txt', 'wt', encoding='utf-8')

for _ in range(100):
    file.write('I love pizza\nI love Python\n')

file.close()
