input = open('input').read().splitlines()

l1 = input
l2 = input
for i in range(len(input[0])):
    qty = [val[i] for val in l1].count('0')
    most_common = int(qty <= len(l1) / 2)
    l1 = [v for v in l1 if len(l1) == 1 or v[i] == str(most_common)]
    l2 = [v for v in l2 if len(l2) == 1 or v[i] == str(int(not most_common))]
print(l1, l2)
print(int(l1[0], 2) * int(l2[0], 2))
