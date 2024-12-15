grid, instructions = open('input').read().split('\n\n')

walls, boxes = set(), set()
robot = 0, 0
positions = {'>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}

for i, line in enumerate(grid.splitlines()):
    for j, cell in enumerate(line):
        if cell == '#':
            walls.add((i, j))
        elif cell == 'O':
            boxes.add((i, j))
        elif cell == '@':
            robot = i, j

def push(dx, dy):
    nx, ny = robot
    moves = []
    while True:
        nx += dx
        ny += dy
        if (nx, ny) in walls:                               # Find a wall first => No move
            return robot, []
        elif (nx, ny) in boxes:                             # Find a box => Add to move list
            moves.append((nx, ny))
        else:                                               # Find a empty spot first => Move robot and boxes
            return (robot[0] + dx, robot[1] + dy), moves

for instruction in ''.join(instructions.splitlines()):
    dx, dy = positions[instruction]
    robot, moves = push(dx, dy)
    for move in moves[::-1]:
        boxes.remove(move)
        boxes.add((move[0] + dx, move[1] + dy))
print(sum(i * 100 + j for i, j in list(boxes)))
