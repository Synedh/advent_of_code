reports = [list(map(int, l.split())) for l in open('input')]

def is_safe(report: list[int]) -> bool:
    if report != sorted(report) and report != sorted(report, reverse=True):
        return False
    return all(0 < abs(a - b) < 4 for a, b in zip(report, report[1:]))

print(sum(is_safe(report) for report in reports))

# from itertools import pairwise

# def is_safe(report: list[int]) -> bool:
#     op = operator.lt if report[0] < report[1] else operator.gt
#     return all((op(a, b) and 1 <= abs(a - b) <= 3) for a, b in pairwise(report))
