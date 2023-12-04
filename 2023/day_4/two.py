cards = open('input').read().splitlines()
qties = [1] * len(cards)

for i, card in enumerate(cards):
    winning, numbers = [set(map(int, n.split())) for n in card.split(':')[1].split('|')]
    valids = len(winning & numbers)
    for j in range(i + 1, i + valids + 1):
        qties[j] += qties[i]
print(sum(qties))
