def get_incorrect_num(values):
    lasts = values[:25]
    for value in values[25:]:
        if not any((value - i) in lasts for i in lasts):
            return value
        lasts = lasts[1:] + [value]
    return 0

values = [int(v) for v in open('input').readlines()]
incorrect = get_incorrect_num(values)
print(incorrect)

for i, value in enumerate(values):
    test = value
    items = [value]
    while test < incorrect:
        i += 1
        test += values[i]
        items.append(values[i])
    if test == incorrect:
        print(max(items) + min(items))
        exit()
