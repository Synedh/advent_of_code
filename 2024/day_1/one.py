l1, l2 = zip(*[map(int, line.split()) for line in open('input')])
print(sum(abs(x - y) for x, y in zip(sorted(l1), sorted(l2))))
