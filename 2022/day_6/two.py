line = open('input').read()
print(next(i for i in range(14, len(line)) if len(set(line[i - 14:i])) == 14))
