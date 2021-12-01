l = [*map(int, open('input'))]
print(sum(a < b for a, b in zip(l, l[3:])))