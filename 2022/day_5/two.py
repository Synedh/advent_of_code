stacks, steps = [lines.splitlines() for lines in open('input').read().split('\n\n')]
cargos = [
    [stack[i] for stack in stacks[::-1] if i <= len(stack) and stack[i] != ' ']
    for i in range(1, len(stacks[-1]), 4)
]
actions = [map(int, step.split()[1::2]) for step in steps]

for qty, a, b in actions:
    cargos[b - 1] += cargos[a - 1][-qty:]
    cargos[a - 1] = cargos[a - 1][:-qty]

print(''.join([cargo[-1] for cargo in cargos]))
