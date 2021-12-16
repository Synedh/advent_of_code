input = 'C0015000016115A2E0802F182340'
bin_input = ''.join(format(int(char, base=16), '#06b')[2:] for char in open('input').read().splitlines()[0])

def parse_literals(binary):
        i = 6
        total = ''
        while True:
            total += binary[i + 1:i + 5]
            if binary[i] == '0':
                i += 5
                break
            i += 5
        return i


def parse_operation(binary):
    version = 0
    if binary[6] == '1':
        subpacket_qty = int(binary[7:18], 2)
        length = -1
        i = 18
    elif binary[6] == '0':
        subpacket_qty = -1
        length = int(binary[7:22], 2)
        i = 22
    subpacket_number = 0
    while i < 22 + length or subpacket_number < subpacket_qty:
        subpacket_number += 1
        subpacket_version, j = parse_packet(binary[i:])
        version += subpacket_version
        i += j
    return version, i


def parse_packet(binary):
    version = int(binary[:3], 2)
    id = int(binary[3:6], 2)
    i = 0
    if id == 4:
        return version, parse_literals(binary)
    else:
        operation_version, i = parse_operation(binary)
        return version + operation_version, i

print(parse_packet(bin_input)[0])
