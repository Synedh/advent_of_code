import re


def parse_rules(color_rules):
    if 'shiny gold' in ''.join([color for _, color in color_rules]):
        return True
    return any(parse_rules(rules[color]) for _, color in color_rules)


rules = {}
for rule in open('input').read().splitlines():
    for bag, subbags in re.findall(r'(.*?) bags contain (.*)\.', rule):
        rules[bag] = re.findall(r'(\d) (.*?) bags?', subbags)

print(sum(parse_rules(color_rules) for color_rules in rules.values()))
