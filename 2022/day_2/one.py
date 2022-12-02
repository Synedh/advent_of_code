print(sum((ord(x) - ord(a) - 1) % 3 * 3 + ord(x) - 87 for a, _, x, _ in open('input')))

total = 0
for p1, _, p2, _ in open('input'):
    p1 = ord(p1) - ord('A')
    p2 = ord(p2) - ord('X')
    total += (p2 - p1 + 1) % 3 * 3 + p2 + 1
print(total)
