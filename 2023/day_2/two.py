import re

def count_max(rounds):
    qties = {'red': 0, 'green': 0, 'blue': 0}
    for round in rounds:
        for qty, color in re.findall(r'(\d+)\s(blue|red|green)', round):
            qties[color] = max(qties[color], int(qty))
    return qties['red'] * qties['green'] * qties['blue']

total = 0
for game in open('input'):
    game_name, rounds = game.split(':')
    total += count_max(rounds.split(';'))
print(total)
