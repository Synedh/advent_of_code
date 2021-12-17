def product(values):
    prod = 1
    for value in values:
        prod *= value
    return prod

def gt(values):
    return int(values[0] > values[1])

def lt(values):
    return int(values[0] < values[1])

def equals(values):
    return int(values[0] == values[1])

def parse_literals(binary):
    i = 6
    total = ''
    while True:
        total += binary[i + 1:i + 5]
        if binary[i] == '0':
            return i + 5, int(total, 2)
        i += 5
    
def parse_operation(binary, operation):
    values = []
    if binary[6] == '1':
        i = 18
        for _ in range(int(binary[7:18], 2)):
            j, value = parse_packet(binary[i:])
            i += j
            values.append(value)
    elif binary[6] == '0':
        i = 22
        while i < 22 + int(binary[7:22], 2):
            j, value = parse_packet(binary[i:])
            i += j
            values.append(value)
    return i, operation(values)

def parse_packet(binary):
    id = int(binary[3:6], 2)
    if id == 4:
        return parse_literals(binary)
    else:
        operations = {0: sum, 1: product, 2: min, 3: max, 5: gt, 6: lt, 7: equals}
        return parse_operation(binary, operations[id])

input = open('input').read().splitlines()[0]
bin_input = ''.join(format(int(char, base=16), '04b') for char in input)
print(parse_packet(bin_input)[-1])
