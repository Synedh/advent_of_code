fishes = [*map(int, open('input').read().split(','))]
for day in range(80):
    print(f'\r{day}', end='')
    for i, fish in enumerate(fishes.copy()):
        if fish == 0:
            fishes[i] = 6
            fishes.append(8)
        else:
            fishes[i] = fish - 1
print()
print(len(fishes))