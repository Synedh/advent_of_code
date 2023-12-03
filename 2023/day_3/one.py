import re

symbol_list = r'!@#$%^&*()_-+={}[]\/'
engine = open('input').read().splitlines()

def has_symbol_neightbour(x, y, symbols):
    for i in [x - 1, x, x + 1]:
        for j in [y - 1, y, y + 1]:
            try:
                if engine[i][j] in symbols:
                    return True
            except IndexError:
                continue
    return False

total = 0
for i, line in enumerate(engine):
    for match in re.finditer('\d+', line):
        has_neightbour = any(has_symbol_neightbour(i, y, symbol_list) for y in range(*match.span()))
        if has_neightbour:
            total += int(match.group())
print(total)
