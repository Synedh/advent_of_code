import re

Xmin, Xmax, Ymin, Ymax = [*map(int, re.findall(r'-?\d+', open('input').read().splitlines()[0]))]

def throw(dx, dy):
    x, y = 0, 0
    yMax = -float('inf')
    while True:
        x += dx
        y += dy
        yMax = max(yMax, y)
        if x in range(Xmin, Xmax + 1) and y in range(Ymin, Ymax + 1):
            return yMax
        if x > Xmax + 1 or y < Ymin:
            return -float('inf')
        dx += (1 if dx < 0 else -1 if dx > 0 else 0)
        dy -= 1

print(max(throw(x, y) for x in range(Xmax) for y in range(Xmax)))
