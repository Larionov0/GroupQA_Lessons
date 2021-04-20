names = ['Bob', 'Klara', 'Alex', 'Been', 'Ann', 'Gena']

print([name[:len(name) // 2] for name in names if len(name) % 2 == 0])
