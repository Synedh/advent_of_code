total = 0
input = open('input').read().strip().splitlines()
for p1, p2, p3 in [input[i:i + 3] for i in range(0, len(input), 3)]:
    commons = set(p1) & set(p2) & set(p3)
    total += sum(ord(value) - 96 if value.islower() else ord(value) - 38 for value in commons)
print(total)



