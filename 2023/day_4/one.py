cards = open('input').read().splitlines()
total = 0

for card in cards:
    winning, numbers = [set(map(int, n.split())) for n in card.split(':')[1].split('|')]
    valids = len(winning & numbers)
    total += int(2 ** (valids - 1))
print(total)
