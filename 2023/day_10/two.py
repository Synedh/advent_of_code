import math

ground = open('input').read().splitlines()
directional_map = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)],
    'S': [(-1, 0), (1, 0), (0, -1), (0, 1)],
    '.': [],
}

def get_start():
    for x, line in enumerate(ground):
        for y, cell in enumerate(line):
            if cell == 'S':
                return x, y

def can_travel(x, y, prev):
    for dx, dy in directional_map[ground[x][y]]:
        newX, newY = x + dx, y + dy
        try:
            if (-dx, -dy) in directional_map[ground[newX][newY]] and (newX, newY) != prev:
                return newX, newY
        except IndexError:
            continue
    return None

def is_in(x, y):
    total = 0
    for dx in [x for x in range(x, -1, -1) if (x, y) in positions]:
        directions = directional_map[ground[dx][y]]
        if ground[dx][y] == '-':
            total += 1
        else:
            total += (directions[0][0] * directions[1][1]) / 2
    return bool(int(total) % 2)

pos = start = get_start()
prev = (None, None)
positions = [start]
while (pos := can_travel(pos[0], pos[1], prev)) != start:
    prev = positions[-1]
    positions.append(pos)

total = 0
for x, line in enumerate(ground):
    for y, cell in enumerate(line):
        if (x, y) not in positions and is_in(x, y):
            total += 1
print(total)
