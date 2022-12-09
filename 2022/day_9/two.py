def update_tail(head: list[int], tail: list[int], prev: list[int], add: bool):
    print(head, tail, prev)
    if abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2:
        return tail
    if add:
        tiles.add(f'{prev[0]},{prev[1]}')
    return prev

with open('input.test') as file:
    lines = [(line.split()[0], int(line.split()[1])) for line in file.read().strip().splitlines()]
head = [0, 0]
tail = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
prev = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
tiles = {'0,0'}
for dir, qty in lines:
    for _ in range(qty):
        prev[0] = head.copy()
        if dir == 'R':
            head[0] += 1
        elif dir == 'D':
            head[1] += 1
        elif dir == 'L':
            head[0] -= 1
        elif dir == 'U':
            head[1] -= 1
        for i in range(len(tail)):
            prev[i + 1] = tail[i].copy()
            tail[i] = update_tail([head, *tail][i], tail[i], prev[i + 1], i == (len(tail) - 1))
    print(head, tail)

        
print(len(tiles))
