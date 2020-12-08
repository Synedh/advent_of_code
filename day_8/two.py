instructions = open('input').read().splitlines()

def execute(op, value, acc, i):
    if op == 'acc':
        return acc + eval(value), i + 1
    elif op == 'jmp':
        return acc, i + eval(value)
    return acc, i + 1

def run(instructions):
    acc = 0
    past = set()
    i = 0
    while i < len(instructions):
        past.add(i)
        acc, i = execute(*instructions[i].split(), acc, i)
        if i in past:
            return False, acc
    return True, acc

for i in range(len(instructions)):
    if 'acc' not in instructions[i]:
        new_inst = instructions.copy()
        new_inst[i] = new_inst[i].replace('jmp', 'n').replace('nop', 'jmp').replace('n', 'nop')
        success, acc = run(new_inst)
        if success:
            break
print(acc)
