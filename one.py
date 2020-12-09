input = open('input').readlines()
lasts = [int(num) for num in input[:25]]

def check_if_build_as_lasts(num, lasts):
    if num <= min(lasts) or num >= 2 * max(lasts):
        return False
    for i in lasts:
        for j in lasts:
            if j != i and i + j == num:
                return True
    return False

for num in input[25:]:
    num = int(num)
    if not check_if_build_as_lasts(num, lasts):
        print(f'notok {num}')
        exit()
    lasts = lasts[1:] + [num]

