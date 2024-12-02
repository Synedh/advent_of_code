reports = [list(map(int, l.split())) for l in open('input')]

def is_safe(report: list[int]) -> bool:
    if report != sorted(report) and report != sorted(report, reverse=True):
        return False
    return all(0 < abs(a - b) < 4 for a, b in zip(report, report[1:]))

print(sum(is_safe(report) or any(is_safe(report[:i] + report[i + 1:]) for i in range(len(report))) for report in reports))
