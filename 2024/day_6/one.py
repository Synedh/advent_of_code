grid = open('input').read().splitlines()

x, y = next((i, j) for i, line in enumerate(grid) for j, val in enumerate(line) if val == '^')
mod = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def crawl_line(x, y, modx, mody):
    pos = set()
    while -1 < x + modx < len(grid) and -1 < y + mody < len(grid[0]):
        if grid[x + modx][y + mody] == '#':
            return x, y, pos, False
        x += modx
        y += mody
        pos.add((x, y))
    return x + modx, y + mody, pos, True

i = 0
pos = {(x, y)}
while True:
    modx, mody = mod[i % 4]
    x, y, new_pos, end = crawl_line(x, y, modx, mody)
    pos |= new_pos
    i += 1
    if end:
        break

print(x, y, len(pos))
