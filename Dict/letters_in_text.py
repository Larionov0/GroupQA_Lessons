# coding: utf-8

text = 'Подсолнечник относится к обширному полиморфному роду Helianthus семейства астровые — Asteraceae. Подсолнечник посевной — однолетнее растение с прямостоячим, грубым, покрытым жесткими волосками стеблем высотой от 0,6 до 2,5 м и мощной корневой системой, проникающей в почву на глубину до 2 — 3 м. Среднее число листьев в разных условиях составляет у среднеспелых сортов 28 — 32, раннеспелых и скороспелых — 24 — 28.'

"""
[
П : 5
о : 3
д : 5
с : 2
л : 6
н : 1
р : 5
т : 1
ш : 1
]
"""

symbols_amounts = {}

for symbol in text:
    if symbol in symbols_amounts:
        symbols_amounts[symbol] += 1
    else:
        symbols_amounts[symbol] = 1


# вывод результата
for symbol, amount in symbols_amounts.items():
    print(symbol, ':', amount)


# ! ДОПОЛНИТЕЛЬНО
# поиск самого частовстречающегося символа
cur_max = 0
cur_symbol = ''
for symbol, amount in symbols_amounts.items():
    if symbol not in [' ', '.', ',']:
        if amount > cur_max:
            cur_max = amount
            cur_symbol = symbol

print('Самый частовстречающийся символ:', cur_symbol, '(',  cur_max,')')
