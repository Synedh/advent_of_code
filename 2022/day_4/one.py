is_in = []
for line in open('input').read().strip().splitlines():
    [p11, p12], [p21, p22] = [map(int, p.split('-')) for p in line.split(',')]
    is_in.append(p11 >= p21 and p12 <= p22 or p21 >= p11 and p22 <= p12)
print(sum(is_in))