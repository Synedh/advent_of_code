import re

def resolve(result, members):
    try:
        mem1, mem2, *mems = members
    except ValueError:
        return members[0] == result
    if mem1 > result:
        return False
    return resolve(result, [mem1 + mem2, *mems]) or resolve(result, [mem1 * mem2, *mems])

total = 0
for line in open('input'):
    result, *members = map(int, re.findall(r'\d+', line))
    if resolve(result, members):
        total += result
print(total)
