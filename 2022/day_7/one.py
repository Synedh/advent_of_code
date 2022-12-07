lines = open('input').read().strip().splitlines()

def exec_line(i=1):
    children = {}
    while i < len(lines):
        line = lines[i]
        i += 1
        if line == '$ cd ..':
            break
        if line.startswith('$ cd'):
            children[line.split()[-1]], i = exec_line(i)
        elif not (line.startswith('dir') or line.startswith('$ ls')):
            children[line.split()[1]] = { 'size': int(line.split()[0]) }
    size = sum(child['size'] for child in children.values())
    return {'children': children, 'size': size}, i

def sizes(tree):
    child_sizes = [sizes(child) for child in tree['children'].values() if child.get('children')]
    return [tree['size'], *[size for child_size in child_sizes for size in child_size]]

tree, _ = exec_line()
print(sum(size for size in sizes(tree) if size <= 100000))
