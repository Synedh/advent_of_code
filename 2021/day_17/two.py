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
            return True
        if x > Xmax + 1 or y < Ymin:
            return False
        dx += (1 if dx < 0 else -1 if dx > 0 else 0)
        dy -= 1

print(sum(throw(x, y) for x in range(Xmax + 1) for y in range(Ymin, Xmax)))
