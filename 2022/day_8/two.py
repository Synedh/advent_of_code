grid = open('input').read().strip().splitlines()
t_grid = [l for l in zip(*grid)]

def nb_visible(h, line):
    i = 0
    for i, value in enumerate(line, start=1):
        if h <= value:
            break
    return i

def mul(iter):
    total = 1
    for val in iter:
        total *= val
    return total

visible = []
for i, line in enumerate(grid[1:-1], start=1):
    for j, cell in enumerate(line[1:-1], start=1):
        lines = [
            line[:j][::-1],
            line[j + 1:],
            t_grid[j][:i][::-1],
            t_grid[j][i + 1:]
        ]
        visible.append(mul(nb_visible(cell, line) for line in lines))
print(max(visible))