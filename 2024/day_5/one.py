from collections import defaultdict

p1, p2 = open('input').read().split('\n\n')
updates = [line.split(',') for line in p2.splitlines()]

orders = defaultdict(list)
for order in p1.splitlines():
    before, after = order.split('|')
    orders[before].append(after)

def check(pages):
    return all(
        after in orders[before]
        for i, before in enumerate(pages)
        for after in pages[i + 1:]
    )

print(sum(int(pages[int(len(pages) / 2)]) for pages in updates if check(pages)))
