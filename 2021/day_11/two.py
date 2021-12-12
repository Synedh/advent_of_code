grid = [[*map(int, list(line))] for line in open('input').read().splitlines()]

def light(x, y):
    if x not in range(10) or y not in range(10):
        return 0
    grid[x][y] += 1
    if grid[x][y] == 10:
        adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
            (0, 1), (1, -1), (1, 0), (1, 1)]
        return 1 + sum(light(x + dx, y + dy) for dx, dy in adj)
    return 0

flashs = 0
i = 1
while True:
    this_flashs = sum(sum(light(x, y) for y in range(10)) for x in range(10))
    if this_flashs == 100:
        break
    flashs += this_flashs
    for x in range(10):
        for y in range(10):
            if grid[x][y] > 9:
                grid[x][y] = 0
    if i == 100:
        print(f'{i} - {flashs}')
    i += 1

print(f'{i} - {this_flashs}')
