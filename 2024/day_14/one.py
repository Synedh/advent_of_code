import re

robots = [map(int, re.findall(r'\-?\d+', l)) for l in open('input')]
width, height = 101, 103
seconds = 100

positions = [((x + dx * seconds) % width, (y + dy * seconds) % height) for x, y, dx, dy in robots]

c1, c2, c3, c4 = 0, 0, 0, 0
for x, y in positions:
    if x < width // 2 and y < height // 2:
        c1 += 1
    elif x > width // 2 and y < height // 2:
        c2 += 1
    elif x < width // 2 and y > height // 2:
        c3 += 1
    elif x > width // 2 and y > height // 2:
        c4 += 1

print(c1 * c2 * c3 * c4)
