total = 0
for line in open('input'):
    values = [int(v) for v in line if 48 <= ord(v) <= 57]
    total += values[0] * 10 + values[-1]
print(total)
