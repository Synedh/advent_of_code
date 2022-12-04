total = 0
input = open('input.test').read().strip().splitlines()
for groups in zip(*(iter(input),) * 3):
    common = set.intersection(*map(set, groups)).pop()
    total += (ord(common) - 96) % 58
print(total)

print(sum((ord(set.intersection(*map(set, groups)).pop()) - 96) % 58 for groups in zip(*(iter(open('input.test').read().strip().splitlines()),) * 3)))