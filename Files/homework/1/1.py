def from_filetxt_in_set(filename):
    file = open(filename, 'rt', encoding='utf-8')
    fileset = set()
    for line in file:
        fileset.update(set(line.split()))
    file.close()
    return fileset


def words_from_tw_files_into_one_file(filename1, filename2, resultfile):
    s1 = from_filetxt_in_set(filename1)
    s2 = from_filetxt_in_set(filename2)

    result_list = s1.intersection(s2)

    result_file = open(resultfile, 'wt', encoding='utf-8')
    result_file.write(' '.join(result_list))
    result_file.close()


words_from_tw_files_into_one_file('f1.txt', 'f2.txt', 'result_file.txt')
