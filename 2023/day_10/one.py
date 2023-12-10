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


pos = start = get_start()
prev = (None, None)
positions = [start]
while (pos := can_travel(pos[0], pos[1], prev)) != start:
    prev = positions[-1]
    positions.append(pos)

print(len(positions))
print(math.ceil(len(positions) / 2))
