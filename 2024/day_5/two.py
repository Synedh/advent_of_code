from collections import defaultdict

p1, p2 = open('input').read().split('\n\n')
updates = [list(map(int, line.split(','))) for line in p2.splitlines()]

orders = defaultdict(list)
for order in p1.splitlines():
    before, after = order.split('|')
    orders[int(before)].append(int(after))

def check(pages):
    return all(
        after in orders[before]
        for i, before in enumerate(pages)
        for after in pages[i + 1:]
    )

total = 0
for pages in updates:
    if check(pages):
        continue
    ordered = [pages[0]]
    for page in pages[1:]:
        for i, ordered_page in enumerate(ordered):
            if ordered_page in orders[page]:
                ordered.insert(i, page)
                break
        else:
            ordered.append(page)
    total += ordered[len(ordered) // 2]
print(total)


# part1 = 0
# part2 = 0
# for pages in updates:
#     sorted_pages = sorted(pages, key=lambda page: -len([order for order in orders[page] if order in pages]))
#     if pages == sorted_pages:
#         part1 += pages[len(pages) // 2]
#     else:
#         part2 += sorted_pages[len(sorted_pages) // 2]
# print('Part 1', part1)
# print('Part 2', part2)
