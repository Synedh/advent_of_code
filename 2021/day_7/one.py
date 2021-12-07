input = [*map(int, open('input').read().split(','))]
print(min(sum(abs(val - i) for val in input) for i in range(min(input), max(input))))
