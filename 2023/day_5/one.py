seeds, *maps = open('input').read().split('\n\n')
seeds = [int(seed) for seed in seeds.split()[1:]]
maps = [[list(map(int, line.split())) for line in m.splitlines()[1:]] for m in maps]

locations = []
for seed in seeds:
    for map in maps:
        for target, start, r in map:
            if seed in range(start, start + r):
                seed += target - start
                break
    locations.append(seed)
print(min(locations))
