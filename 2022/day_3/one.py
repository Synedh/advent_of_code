total = 0
for line in open('input').read().strip().splitlines():
    middle = len(line) // 2
    p1, p2 = set(line[middle:]), set(line[:middle])
    total += sum(ord(value) - 96 if value.islower() else ord(value) - 38 for value in p1 & p2)
print(total)



