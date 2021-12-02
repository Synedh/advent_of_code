x, y = 0, 0
for line in open('input').readlines():
    line = line.split()
    if line[0] == 'forward':
        x += int(line[1])
    if line[0] == 'up':
        y -= int(line[1])
    if line[0] == 'down':
        y += int(line[1])
print(x * y)