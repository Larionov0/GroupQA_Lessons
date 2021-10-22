# eval("for i in range(10): print(i)")
# eval('if 2 > 1: print("yes")')

for a in range(10):
    eval('print(a) if a < 5 else print("No")')
