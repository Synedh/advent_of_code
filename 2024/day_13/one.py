import re

systems = [map(int, re.findall(r'\d+', system)) for system in open('input').read().split('\n\n')]

def system_solve(a1, b1, c1, a2, b2, c2):
    y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
    x = (c1 - b1 * y) / a1
    return x, y

total = 0
for a1, a2, b1, b2, c1, c2 in systems:
    x, y = system_solve(a1, b1, c1, a2, b2, c2)
    if int(x) == x and int(y) == y:
        total += 3 * x + y

print(int(total))
