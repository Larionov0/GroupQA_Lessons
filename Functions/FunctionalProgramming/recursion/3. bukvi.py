def count_glas(word) -> int:
    """
    f('vovka') -> 0 + f('ovka')
    f('ovka') -> 1 + f('vka')
    f('vka') -> 0 + f('ka')
    f('ka') -> 0 + f('a')
    f('a') -> 1 + f('')

    ! f('') -> 0
    """
    if word == '':
        return 0

    letter = word[0]
    if letter in ['a', 'e', 'y', 'u', 'i', 'o']:
        num = 1
    else:
        num = 0
    return num + count_glas(word[1:])


def count_glas_with_state(word, counter=0):
    if word == '':
        return counter
    return count_glas_with_state(word[1:], counter + (1 if word[0] in ['a', 'e', 'y', 'u', 'i', 'o'] else 0))


print(count_glas_with_state('aboba'))
