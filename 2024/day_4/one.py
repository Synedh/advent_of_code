data = [list(l) for l in open('input').read().splitlines()]

inverted = list(zip(*data))
diag = [[] for _ in range(len(data) + len(data[0]) - 1)]
antidiag = [[] for _ in range(len(diag))]

min_antidiag = -len(data) + 1
for y, row in enumerate(data):
    for x, val in enumerate(row):
        diag[x + y].append(val)
        antidiag[x - y - min_antidiag].append(val)

count = 0
for line in data + inverted + diag + antidiag:
    line = ''.join(line)
    count += line.count('XMAS') + line.count('SAMX')

print(count)
