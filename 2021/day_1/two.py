l = [int(i) for i in open('input').read().splitlines()]
print(sum(sum(l[i:i + 3]) < sum(l[i + 1:i + 4]) for i, _ in enumerate(l[:-3])))