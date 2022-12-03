import re
from math import ceil

def split(fullnum, i):
    num = int(fullnum[i])
    splitted_num = [ '[', str(num // 2), str(ceil(num / 2)), ']']
    return fullnum[:i] + splitted_num + fullnum[i + 1:]

def explode(fullnum, i):
    def nearest_int(i, order=1):
        while 0 < i < len(fullnum) - 1:
            i += order
            if fullnum[i].isdigit():
                return i
        return None
    
    nearest_left = nearest_int(i, -1)
    nearest_right = nearest_int(i + 1)
    if nearest_left:
        fullnum[nearest_left] = str(int(fullnum[nearest_left]) + int(fullnum[i]))
    if nearest_right:
        fullnum[nearest_right] = str(int(fullnum[nearest_right]) + int(fullnum[i + 1]))
    return fullnum[:i - 1] + ['0'] + fullnum[i + 3:]

def reduce_step(sfnum):
    depth = 0
    for pos in range(len(sfnum)):
        if sfnum[pos] == "[": depth += 1
        elif sfnum[pos] == "]": depth -= 1
        elif depth == 5: return explode(sfnum, pos)

    for pos in range(len(sfnum)):
        if sfnum[pos].isdigit() and int(sfnum[pos]) >= 10: return split(sfnum, pos)
    raise EOFError

def reduce_fully(sfnum):
    while True:
        try: sfnum = reduce_step(sfnum)
        except EOFError: break
    return sfnum

def check(fullnum):
    i = 0
    depth = 0
    while i < len(fullnum):
        if fullnum[i] == '[':
            depth += 1
            i += 1
        elif fullnum[i] == ']':
            depth -= 1
            i += 1
        else:
            if depth > 4:
                fullnum = explode(fullnum, i)
                i = 0
                depth = 0
            elif int(fullnum[i]) > 9:
                fullnum = split(fullnum, i)
                i = 0
                depth = 0
            else:
                i += 1
    return fullnum

def add(a, b):
    return reduce_fully(['['] + a + b + [']'])

def reformat(fullnum):
    i = 0
    while i + 1 < len(fullnum):
        if (fullnum[i].isdigit() or fullnum[i] == ']') and fullnum[i + 1] != ']':
            fullnum = fullnum[:i + 1] + [','] + fullnum[i + 1:]
        i += 1
    return eval(''.join(fullnum))
    
def format_num(value):
    return re.findall('\d|\[|\]', value)


def magnitude(list_num: int | list):
    if isinstance(list_num, int):
        return list_num
    return 3 * magnitude(list_num[0]) + 2 * magnitude(list_num[1])



result, *values = [format_num(line) for line in open('input').read().splitlines()]
for value in values:
    result = add(result, value)
print(magnitude(reformat(result)))

values = [format_num(line) for line in open('input').read().splitlines()]
print(max(magnitude(reformat(add(values[i], values[j]))) for i in range(len(values)) for j in range(len(values)) if i != j))
