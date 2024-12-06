grid = [list(l) for l in open('input').read().splitlines()]

guard = next((i, j) for i, line in enumerate(grid) for j, val in enumerate(line) if val == '^')
orientations = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def crawl_line(grid, x, y, modx, mody):
    pos = set()
    while -1 < x + modx < len(grid) and -1 < y + mody < len(grid[0]):
        if grid[x + modx][y + mody] == '#':
            return x, y, pos, False
        x += modx
        y += mody
        pos.add((x, y))
    return x + modx, y + mody, pos, True

def crawl_grid(grid, x, y):
    i = 0
    pos = {(x, y)}
    paths = []
    while True:
        mod = orientations[i % 4]
        x, y, new_pos, end = crawl_line(grid, x, y, *mod)
        path = (x, y, mod)
        if path in paths:
            return pos, True
        paths.append(path)
        pos |= new_pos
        i += 1
        if end:
            break
    return pos, False

pos_set, _ = crawl_grid(grid, *guard)
allow_loop = 0
for i, (x, y) in enumerate(list(pos_set)):
    new_grid = [line[:] for line in grid]
    new_grid[x][y] = '#'
    _, loop = crawl_grid(new_grid, *guard)
    allow_loop += int(loop)
print(allow_loop)
