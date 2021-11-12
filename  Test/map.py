# def preobraz(word):
#     return '<' + word + '>'


words = ['thumb', 'hand', 'head', 'leg']

#  'lol' -> '<lol>'

new_list = list(map(lambda word: '<' + word + '>', words))
print(new_list)
