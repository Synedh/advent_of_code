from collections import defaultdict

grid = open('input').read().splitlines()
antennas = defaultdict(list)

def add_coords(a, b):
    return a[0] + b[0], a[1] + b[1]

def sub_coords(a, b):
    return a[0] - b[0], a[1] - b[1]

def is_valid(x, y):
    return -1 < x < len(grid) and -1 < y < len(grid[0])

for x, line in enumerate(grid):
    for y, val in enumerate(line):
        if val != '.':
            antennas[val].append((x, y))


antinodes = set()
for frequency, values in antennas.items():
    for i, e1 in enumerate(values):
        for e2 in values[i + 1:]:
            antinodes.add(e1)
            antinodes.add(e2)
            diff = sub_coords(e1, e2)
            antinode = e1
            while is_valid(*(antinode := add_coords(antinode, diff))):
                antinodes.add(antinode)
            antinode = e2
            while is_valid(*(antinode := sub_coords(antinode, diff))):
                antinodes.add(antinode)
print(len(antinodes))
