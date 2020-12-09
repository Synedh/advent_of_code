values = [int(v) for v in open('input').readlines()]

lasts = values[:25]
for value in values[25:]:
    if not any((value - j) in lasts for j in lasts):
        print(value)
        exit()
    lasts = lasts[1:] + [value]

