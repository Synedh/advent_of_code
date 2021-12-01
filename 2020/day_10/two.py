values = sorted(int(line) for line in open('input'))
values = [0] + values + [values[-1] + 3]
diffs = [a - b for a, b in zip(values[1:], values[:-1])]

print(''.join('-' if x==1 else '*' for x in diffs).split('*'))

# def get_arrangements(values):
#     nexts = [values[values.index(v):] for v in values[1:4] if v <= values[0] + 3]
#     if nexts == []:
#         return 1
#     return sum(1 * get_arrangements(n) for n in nexts)

# print(get_arrangements(values))
# print(diffs.count(1) * diffs.count(3))