print(sum((ord(p2) - 88) * 3 + (ord(p1) + ord(p2) - 1) % 3 + 1 for p1, _, p2, _ in open('input')))

total = 0
for p1, _, p2, _ in open('input'):
    p1 = ord(p1) - ord('A')
    p2 = ord(p2) - ord('X')
    total += p2 * 3 + (p1 + p2 - 1) % 3 + 1
print(total)
