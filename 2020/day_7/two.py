import re


def parse_rules(color_rules):
    if color_rules == []:
        return 1
    return 1 + sum(int(qty) * parse_rules(rules[color]) for qty, color in color_rules)


rules = {}
for rule in open('input').read().splitlines():
    for bag, subbags in re.findall(r'(.*?) bags contain (.*)\.', rule):
        rules[bag] = re.findall(r'(\d) (.*?) bags?', subbags)

print(parse_rules(rules['shiny gold']) - 1)
