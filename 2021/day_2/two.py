x, y, aim = 0, 0, 0
for line in open('input').readlines():
    way, value = line.split()
    value = int(value)
    if way == 'forward':
        x += value
        y += aim * value
    if way == 'up':
        aim -= value
    if way == 'down':
        aim += value
print(x * y)