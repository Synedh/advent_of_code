template, rules = open('input').read().split('\n\n')
rules = dict(rule.split(' -> ') for rule in rules.splitlines())
pairs = { pair: template.count(pair) for pair in rules }
chars = { char: template.count(char) for char in rules.values() }

for i in range(40):
    for pair, value in pairs.copy().items():
        pairs[pair] -= value
        pairs[pair[0] + rules[pair]] += value
        pairs[rules[pair] + pair[1]] += value
        chars[rules[pair]] +=  value
print(max(chars.values()) - min(chars.values()))
