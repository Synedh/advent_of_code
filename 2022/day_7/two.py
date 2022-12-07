import json
from itertools import chain

lines = open('input').read().strip().splitlines()

def exec_line(i: int=0):
    children = {}
    while i < len(lines):
        line = lines[i]
        i += 1
        if line.startswith('$ cd'):
            if line.split()[-1] == '..':
                break
            children[line.split()[-1]], i = exec_line(i)
        elif line.startswith('$ ls'):
            continue
        else:
            value, name = line.split()
            if value != 'dir':
                children[name] = { 'size': int(value) }
    size = sum(child['size'] for child in children.values())
    return {'children': children, 'size': size}, i

def sizes(tree):
    child_sizes = [sizes(child) for child in tree['children'].values() if child.get('children')]
    return [tree['size']] + list(chain(*[ele if isinstance(ele, list) else [ele] for ele in child_sizes]))

tree, _ = exec_line(1)
folder_sizes = sizes(tree)

print(min(size for size in folder_sizes if size >= max(folder_sizes) - 30000000))
