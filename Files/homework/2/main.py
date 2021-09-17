def from_text_to_files_with_word_size(some_file):
    word_list = []
    file = open(some_file, 'rt', encoding='utf-8')

    for line in file:
        word_list.extend(line.strip().split(', '))

    file.close()

    for word in word_list:
        filename = word + '.txt'
        file = open(filename, 'wt', encoding='utf-8')
        file.write(str(len(word)))
        file.close()


from_text_to_files_with_word_size('f1.txt')
