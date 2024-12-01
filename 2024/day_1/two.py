l1, l2 = zip(*[map(int, line.split()) for line in open('input')])
print(sum(x for x in l2 if x in l1))
