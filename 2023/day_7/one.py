from collections import Counter

card_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def order_hand(hand):
    hand_count = sorted(list(Counter(hand).values()), reverse=True)
    hand_type = f'{"".join(map(str, hand_count)):<5}'
    hand_cards = ''.join(f'{card_values.index(card):>2}' for card in hand)
    return hand_type + hand_cards

sorted_hands = sorted(
    open('input').read().splitlines(),
    key=lambda line: order_hand(line.split()[0])
)
print(sorted_hands)
print(sum(int(hand.split()[1]) * (i + 1) for i, hand in enumerate(sorted_hands)))
