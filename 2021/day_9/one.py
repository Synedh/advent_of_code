def is_lower(matrice, i, j):
    val = int(matrice[i][j])
    nearests = []
    for a, b in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
        try:
            nearests.append(int(matrice[a][b]))
        except IndexError:
            pass
    if val < min(nearests):
        return val + 1
    return 0

matrice = open('input').read().split('\n')
total = 0
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        total += is_lower(matrice, i, j)
print(total)
