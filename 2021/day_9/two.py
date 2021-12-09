def get_basin(matrice, i, j):
    if 0 <= i < len(matrice) and 0 <= j < len(matrice[i]) and matrice[i][j] != '9':
        matrice[i][j] = '9'
        return (
            1
            + get_basin(matrice, i - 1, j)
            + get_basin(matrice, i + 1, j)
            + get_basin(matrice, i, j - 1)
            + get_basin(matrice, i, j + 1)
        )
    return 0

matrice = [*map(list, open('input').read().split('\n'))]
basins = []
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        basins.append(get_basin(matrice, i, j))
basins.sort(reverse=True)
print(basins[0] * basins[1] * basins[2])
