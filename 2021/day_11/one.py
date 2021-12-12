input = [[*map(int, list(line))] for line in open('input').read().splitlines()]

def light(x, y):
    if x not in range(10) or y not in range(10):
        return 0
    input[x][y] += 1
    if input[x][y] == 10:
        return 1 + sum(light(x + dx, y + dy) for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])
    return 0

flashs = 0
for _ in range(100):
    flashs += sum(sum(light(x, y) for y in range(10)) for x in range(10))
    for x in range(10):
        for y in range(10):
            if input[x][y] > 9:
                input[x][y] = 0

print(flashs)
