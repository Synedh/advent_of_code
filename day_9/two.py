def get_target(values):
    lasts = values[:25]
    for value in values[25:]:
        if not any((value - i) in lasts for i in lasts):
            return value
        lasts = lasts[1:] + [value]
    return -1

values = [int(v) for v in open('input')]
target = get_target(values)
print(target)

for i, value in enumerate(values):
    items = [value]
    while sum(items) < target:
        i += 1
        items.append(values[i])
    if sum(items) == target:
        print(max(items) + min(items))
        exit()
