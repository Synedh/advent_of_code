l = open('input').read().splitlines()
print(sum(item > l[i] for i, item in enumerate(l[1:])))