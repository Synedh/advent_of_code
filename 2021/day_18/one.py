import re
from math import ceil

input = '[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]\n[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]'

def split(fullnum, i):
    num = fullnum[i]
    splitted_num = [
        {'value': num['value'] // 2, 'depth': num['depth'] + 1},
        {'value': ceil(num['value'] / 2), 'depth': num['depth'] + 1}
    ]
    print('split', fullnum[:i] + splitted_num + fullnum[i + 1:])
    return fullnum[:i] + splitted_num + fullnum[i + 1:]

def explode(fullnum, i):
    if i >= 1:
        fullnum[i - 1]['value'] += fullnum[i]['value']
    if i + 2 < len(fullnum):
        fullnum[i + 2]['value'] += fullnum[i + 1]['value']
    fullnum[i]['value'] = 0
    fullnum[i]['depth'] -= 1
    print('explode', fullnum[:i + 1] + fullnum[i + 2:])
    return fullnum[:i + 1] + fullnum[i + 2:]

def add(a, b):
    num = a + b
    for value in num:
        value['depth'] += 1
    return check(num)

def check(fullnum):
    i = 0
    length = len(fullnum)
    while i < len(fullnum):
        if fullnum[i]['depth'] > 4:
            fullnum = explode(fullnum, i)
            i = 0
            length = len(fullnum)
        elif fullnum[i]['value'] > 9:
            fullnum = split(fullnum, i)
            i = 0
            length = len(fullnum)
        else:
            i += 1
    return fullnum

def reformat(fullnum):
    value = ''
    depth = 0
    pair = False
    for num in fullnum:
        while depth < num[depth]:
            value += '['
        
    
def format_num(value):
    depth = 0
    values = []
    for char in value:
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        elif char == ',':
            pass
        else:
            values.append({'value': int(char), 'depth': depth})
    return values

# value = format_num(input.splitlines()[0])
# for string in input.splitlines()[1:]:
#     value = add(value, format_num(string))
# print(value)

print(add(format_num('[[[[4,3],4],4],[7,[[8,4],9]]]'), format_num('[1,1]')))
