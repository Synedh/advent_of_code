input = open('input').read().splitlines()

l1, l2 = input, input
for i in range(len(input[0])):
    most_common_l1 = int([val[i] for val in l1].count('0') <= len(l1) / 2)
    less_common_l2 = int([val[i] for val in l2].count('0') > len(l2) / 2)
    l1 = [v for v in l1 if len(l1) == 1 or v[i] == str(most_common_l1)]
    l2 = [v for v in l2 if len(l2) == 1 or v[i] == str(less_common_l2)]
print(int(l1[0], 2) * int(l2[0], 2))
