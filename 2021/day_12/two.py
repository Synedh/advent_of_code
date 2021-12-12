caves = {}
for line in open('input').read().splitlines():
    node, next = line.split('-')
    caves[node] = caves.get(node, []) + [next]
    caves[next] = caves.get(next, []) + [node]

def walkthrough(cave, visited, has_visited):
    if cave == 'end':
        return 1
    return sum(
        walkthrough(next_cave, visited + [cave], has_visited or cave.islower() and cave in visited)
        for next_cave in caves[cave]
        if next_cave.isupper() or next_cave != 'start' and (not has_visited or next_cave not in visited)
    )

print(walkthrough('start', [], False))
