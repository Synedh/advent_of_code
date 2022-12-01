print(sum(sorted(sum(map(int, cals.split('\n'))) for cals in open('input').read().strip().split('\n\n'))[-3:]))
