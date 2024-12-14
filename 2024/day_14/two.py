import re

robots = [list(map(int, re.findall(r'\-?\d+', l))) for l in open('input').read().splitlines()]
width, height = 101, 103
seconds = 100000

for s in range(seconds):
    positions = [((x + dx * s) % width, (y + dy * s) % height) for x, y, dx, dy in robots]
    for row in range(height):
        robots_line = [(x, y) for (x, y) in positions if y == row]
        if len(robots_line) > 10:
            robots_line = sorted(robots_line)
            contigus = sum(x2 - x1 == 1 for (x1, _), (x2, _) in zip(robots_line, robots_line[1:]))
            if contigus > 15:
                print(s, robots_line)
                exit()
