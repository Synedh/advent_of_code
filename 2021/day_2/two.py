x, y, aim = 0, 0, 0
for line in open('input'):
    match line.split():
        case ('forward', int(v) as value):
            x += value
            y += aim * value
        case ('up', value):
            aim -= int(value)
        case ('down', value):
            aim += int(value)
print(x * y)