from collections import Counter

template, rules = input.split('\n\n')
rules = dict(rule.split(' -> ') for rule in rules.splitlines())
pairs = { pair: 0 for pair in rules }

for i in range(len(template) - 1):
    pairs[template[i:i+2]] += 1
count = Counter(template)
for i in range(10):
    for pair, value in pairs.copy().items():
        pairs[pair] -= value
        pairs[pair[0] + rules[pair]] += value
        pairs[rules[pair] + pair[1]] += value
        count[rules[pair]] = count.get(rules[pair], 0) + value
qties = count.values()
print(max(qties) - min(qties))
