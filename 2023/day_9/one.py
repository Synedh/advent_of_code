report = [[*map(int, line.split())] for line in open('input')]

def rec_derivative(seq):
    dv = [y - x for x, y in zip(seq, seq[1:])]
    return seq[-1] + (rec_derivative(dv) if any(dv) else 0)

print(sum(rec_derivative(line) for line in report))
