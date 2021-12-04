nums, *boards = open('input').read().split('\n\n')
boards = [[row.split() for row in board.split('\n')] for board in boards]

def check_num(num):
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, value in enumerate(row):
                if value == num:
                    boards[i][j][k] = None

def check_boards():
    for board in boards:
        if (any(not any(row) for row in board)
            or any(not any(col) for col in zip(*board))):
            return board
    return None

for num in nums.split(','):
    check_num(num)
    while len(boards) and (board := check_boards()):
        boards.remove(board)
    if not len(boards):
        break
print(sum(sum(int(value) for value in row if value) for row in board) * int(num))
