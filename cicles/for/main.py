lst = ['огурец', "петрушка", "бобы", "помидор", "клюква"]
print(lst)
print()
i = 0
letter = 'о'
print('Индексы:')
for veg in lst:
    if letter in veg:
        print(i)
    else:
        pass
    i += 1
