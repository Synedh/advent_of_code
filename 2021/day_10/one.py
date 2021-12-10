pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
values = {')': 3, ']': 57, '}': 1197, '>': 25137, None: 0}

def parser(line):
    closers = []
    for char in line:
        if char in pairs:
            closers.append(pairs[char])
        elif char == closers[-1]:
            closers.pop()
        else:
            return char
    return None

print(sum(values[parser(line)] for line in open('input').read().split('\n')))
