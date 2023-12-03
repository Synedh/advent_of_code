import re

load = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def is_game_ok(rounds):
    for round in rounds:
        for qty, color in re.findall(r'(\d+)\s(blue|red|green)', round):
            if load[color] < int(qty):
                return False
    return True

total = 0
for game in open('input'):
    game_name, rounds = game.split(':')
    if is_game_ok(rounds.split(';')):
        total += int(game_name.split(' ')[-1])
print(total)
