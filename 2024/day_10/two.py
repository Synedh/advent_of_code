topo = [list(map(int, l)) for l in open('input').read().splitlines()]
trailheads = [(x, y) for x, line in enumerate(topo) for y, val in enumerate(line) if val == 0]

def get_neightbours(x, y):
    neightbours = []
    for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
        if -1 < x + dx < len(topo) and -1 < y + dy < len(topo[0]):
            neightbours.append((x + dx, y + dy))
    return neightbours

def walk_path(x, y, height):
    if topo[x][y] == 9:
        return 1
    paths = 0
    for x, y in get_neightbours(x, y):
        if topo[x][y] == height + 1:
            paths += walk_path(x, y, height + 1)
    return paths

print(sum(walk_path(*trailhead, 0) for trailhead in trailheads))
