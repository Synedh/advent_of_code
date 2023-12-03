import re
from collections import defaultdict
from math import prod

symbol_list = r'!@#$%^&*()_-+={}[]\/'
engine = open('input').read().splitlines()

def has_symbol_neightbour(x, y, symbols):
    adjacent = {(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)}
    for dx, dy in adjacent:
            try:
                if engine[x + dx][y + dy] in symbols:
                    return x + dx, y + dy
            except IndexError:
                continue
    return None

gears = defaultdict(list)
for i, line in enumerate(engine):
    for match in re.finditer('\d+', line):
        neightbours = set(has_symbol_neightbour(i, y, '*') for y in range(*match.span()))
        for neightbour in [v for v in neightbours if v]:
            gears[str(neightbour)].append(int(match.group()))
print(sum(prod(numbers) for numbers in gears.values() if len(numbers) == 2))
