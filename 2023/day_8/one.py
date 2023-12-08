from itertools import cycle

directions, _, *str_ways = open('input').read().splitlines()
c = cycle(int(d == 'R') for d in directions)
ways = {way[0:3]: (way[7:10], way[12:15]) for way in str_ways}

current = 'AAA'
total = 0
while current != 'ZZZ':
    total += 1
    current = ways[current][next(c)]
print(total)