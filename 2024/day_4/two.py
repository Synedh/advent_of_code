data = open('input').read().splitlines()

count = 0
for i, line in enumerate(data[1:-1], start=1):
    for j, val in enumerate(line[1:-1], start=1):
        if val != 'A':
            continue
        valid = ['MSMS', 'SMSM', 'SMMS', 'MSSM']
        if data[i - 1][j - 1] + data[i + 1][j + 1] + data[i + 1][j - 1] + data[i - 1][j + 1] in valid:
            count += 1

print(count)
