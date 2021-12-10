pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
values = {')': 1, ']': 2, '}': 3, '>': 4}

def parser(line):
    closers = []
    for char in line:
        if char in pairs:
            closers.append(pairs[char])
        elif char == closers[-1]:
            closers.pop()
        else:
            return []
    return closers

totals = []
for line in open('input').read().split('\n'):
    if len(incompletes := parser(line)[::-1]):
        total = 0
        for closer in incompletes:
            total = total * 5 + values[closer]
        totals.append(total)
print(sorted(totals)[len(totals) // 2])
