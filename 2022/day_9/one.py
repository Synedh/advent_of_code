def update_tail(head: list[int], tail: list[int], prev: list[int]):
    if abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2:
        return tail
    tiles.add(str(prev))
    return prev

with open('input') as file:
    lines = [(line.split()[0], int(line.split()[1])) for line in file.read().strip().splitlines()]
head, tail, tiles = [0, 0], [0, 0], {'[0, 0]'}
for dir, qty in lines:
    for _ in range(qty):
        prev = head.copy()
        if dir == 'R':
            head[0] += 1
        elif dir == 'D':
            head[1] += 1
        elif dir == 'L':
            head[0] -= 1
        elif dir == 'U':
            head[1] -= 1
        tail = update_tail(head, tail, prev)
        
print(len(tiles))