from collections import Counter

def decode(patterns):
    code = ['' for _ in range(7)]
    sorted_values = ['' for _ in range(10)]
    counter = Counter(patterns)
    counter_keys = list(counter.keys())
    counter_values = list(counter.values())
    code[2] = counter_keys[counter_values.index(9)]
    code[4] = counter_keys[counter_values.index(4)]
    code[5] = counter_keys[counter_values.index(6)]
    for value in patterns.split():
        match len(value):
            case 2:
                sorted_values[1] = value
            case 3:
                sorted_values[7] = value
            case 4:
                sorted_values[4] = value
            case 7:
                sorted_values[8] = value
    code[0] = (set(sorted_values[7]) - set(sorted_values[1])).pop()
    code[1] = [key for key, value in counter.items() if key != code[0] and value == 8][0]
    code[3] = [key for key, value in counter.items() if key not in sorted_values[4] and value == 7][0]
    code[6] = [key for key, value in counter.items() if key in sorted_values[4] and value == 7][0]

    sorted_values[0] = code[0] + code[1] + code[2] + code[3] + code[4] + code[5]
    sorted_values[2] = code[0] + code[1] + code[3] + code[4] + code[6]
    sorted_values[3] = code[0] + code[1] + code[2] + code[3] + code[6]
    sorted_values[5] = code[0] + code[2] + code[3] + code[5] + code[6]
    sorted_values[6] = code[0] + code[2] + code[3] + code[4] + code[5] + code[6]
    sorted_values[9] = code[0] + code[1] + code[2] + code[3] + code[5] + code[6]
    return [''.join(sorted(value)) for value in sorted_values]

total = 0
for line in open('input').read().split('\n'):
    digits = decode(line.split('|')[0])
    number = 0
    for value in line.split('|')[1].split():
        number = 10 * number + digits.index(''.join(sorted(value)))
    total += number
print(total)

        