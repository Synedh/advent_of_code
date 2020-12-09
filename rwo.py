def check_if_build_as_lasts(num, lasts):
    if num <= min(lasts) or num >= 2 * max(lasts):
        return False
    for i in lasts:
        for j in lasts:
            if j != i and i + j == num:
                return True
    return False

def get_incorrect_num(input):
    lasts = [int(num) for num in input[:25]]
    for num in input[25:]:
        num = int(num)
        if not check_if_build_as_lasts(num, lasts):
            return num
        lasts = lasts[1:] + [num]
    return 0

input = open('input').readlines()
num = get_incorrect_num(input)
print(num)
for i, value in enumerate(input):
    test = int(value)
    items = [int(value)]
    while test < num:
        i += 1
        test += int(input[i])
        items.append(int(input[i]))
    if test == num:
        print(max(items) + min(items))
        exit()
