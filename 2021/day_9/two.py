matrice = [*map(list, open('input').read().split('\n'))]

def get_basin(x, y):
    if x in range(len(matrice)) and y in range(len(matrice[x])) and matrice[x][y] != '9':
        matrice[x][y] = '9'
        return 1 + sum(get_basin(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)])
    return 0

basins = []
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        basins.append(get_basin(i, j))
basins.sort(reverse=True)
print(basins[0] * basins[1] * basins[2])
