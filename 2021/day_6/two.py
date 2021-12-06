fishes = open('input').read().split(',')
olds = [fishes.count(str(i)) for i in range(9)]
for day in range(256):
    # olds[7] += olds[0]
    # olds = olds[1:] + olds[:1]
    olds[(day + 7) % 9] += olds[day % 9]
print(sum(olds))