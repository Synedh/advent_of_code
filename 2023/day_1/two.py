map_table = {
    'one': 1, '1': 1,
    'two': 2, '2': 2,
    'three': 3, '3': 3,
    'four': 4, '4': 4,
    'five': 5, '5': 5,
    'six': 6, '6': 6,
    'seven': 7, '7': 7,
    'eight': 8, '8': 8,
    'nine': 9, '9': 9
}

total = 0
for line in open('input'):
    ints = []
    for i in range(len(line)):
        ints += [map_table[key] for key in map_table if line[i:].startswith(key)]
    total += ints[0] * 10 + ints[-1]
print(total)
