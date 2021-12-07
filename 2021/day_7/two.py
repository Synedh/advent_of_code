input = [*map(int ,open('input').read().split(','))]
print(min(sum((abs(val - i) ** 2 + abs(val - i)) // 2 for val in input) for i in range(min(input), max(input))))
