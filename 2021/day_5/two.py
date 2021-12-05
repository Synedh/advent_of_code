import re
from collections import Counter

input = [[*map(int, re.findall(r'\d+', val))] for val in open('input').read().splitlines()]
cells = []
for x0, y0, x1, y1 in input:
    dx = 0 if x0 == x1 else 1 if x0 < x1 else -1
    dy = 0 if y0 == y1 else 1 if y0 < y1 else -1
    length = 1 + max(abs(x0 - x1), abs(y0 - y1))
    cells += [(x0 + i * dx, y0 + i * dy) for i in range(length)]
print(sum(count > 1 for count in Counter(cells).values()))
