grid = open('input').read().strip().splitlines()
t_grid = [l for l in zip(*grid)]

visible = []
for i, line in enumerate(grid[1:-1], start=1):
    for j, cell in enumerate(line[1:-1], start=1):
        visible.append(
            cell > max(line[:j]) 
            or cell > max(line[j + 1:])
            or cell > max(t_grid[j][:i])
            or cell > max(t_grid[j][i + 1:])
        )
print(2 * (len(grid) - 1) + 2 * (len(t_grid) - 1) + sum(visible))