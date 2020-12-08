instructions = open('input').read().splitlines()

def execute(op, value, acc, i):
    if op == 'acc':
        return acc + eval(value), i + 1
    elif op == 'jmp':
        return acc, i + eval(value)
    return acc, i + 1

acc = 0
past = []
i = 0
while i not in past and i < len(instructions):
    past.append(i)
    acc, i = execute(*instructions[i].split(), acc, i)
print(acc)
