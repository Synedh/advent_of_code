values = sorted(int(line) for line in open('input'))
values = [0] + values + [values[-1] + 3]
diffs = [a - b for a, b in zip(values[1:], values[:-1])]
print(diffs.count(1) * diffs.count(3))