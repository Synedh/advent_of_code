grid, instructions = open('input').read().split('\n\n')

walls, boxes = set(), set()
x, y = 0, 0
positions = {'>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}

for i, line in enumerate(grid.splitlines()):
    for j, cell in enumerate(line):
        if cell == '#':
            walls.add(((i, j * 2), (i, j * 2 + 1)))
        elif cell == 'O':
            boxes.add(((i, j * 2), (i, j * 2 + 1)))
        elif cell == '@':
            x, y = i, j * 2

def push(x, y, dx, dy, moves) -> (bool, set):
    if any(filter(lambda move: (x, y) in move, moves)):
        return True
    if any(filter(lambda wall: (x, y) in wall, walls)):
        return False
    elif box := next((box for box in boxes if (x, y) in box), ()):
        (x1, y1), (x2, y2) = box
        moves.append(box)
        return push(x1 + dx, y1 + dy, dx, dy, moves) and push(x2 + dx, y2 + dy, dx, dy, moves)
    else:
        return True


for instruction in ''.join(instructions.splitlines()):
    dx, dy = positions[instruction]
    moves = []
    do_move = push(x + dx, y + dy, dx, dy, moves)
    if do_move:
        x += dx
        y += dy
        for box1, box2 in moves[::-1]:
            boxes.remove((box1, box2))
            boxes.add(((box1[0] + dx, box1[1] + dy), (box2[0] + dx, box2[1] + dy)))

print(sum(i * 100 + j for (i, j), _ in list(boxes)))
