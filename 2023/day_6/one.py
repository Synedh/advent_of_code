runs = zip(*[map(int, l.split()[1:]) for l in open('input')])

total = 1
for time, distance in runs:
    total *= sum(i * (time - i) > distance for i in range(time))
print(total)
