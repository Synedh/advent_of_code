import re

data = re.sub(r'don\'t\(\).*?(?:do\(\)|$)', '', open('input').read(), flags=re.DOTALL)
print(sum(int(x) * int(y) for x, y in re.findall(r'mul\((\d+),(\d+)\)', data)))


# finds = re.findall(r'mul\((\d+),(\d+)\)|(do)\(\)|(don\'t)\(\)', open('input').read())
# total = 0
# skip = False
# for x, y, do, dont in finds:
#     if do:
#         skip = False
#     elif dont:
#         skip = True
#     elif not skip:
#         total += int(x) * int(y)
# print(total)
