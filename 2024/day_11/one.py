stones = list(map(int, open('input').readline().strip().split()))

memory = {}

def solve(stone, blinks):
    if blinks == 0:
        return 1
    elif (stone, blinks) in memory:
        return memory[(stone, blinks)]
    elif stone == 0:
        val = solve(1, blinks - 1)
    elif not len(str_int := str(stone)) % 2:
        mid = len(str_int) // 2
        val = solve(int(str_int[:mid]), blinks - 1) + solve(int(str_int[mid:]), blinks - 1)
    else:
        val = solve(stone * 2024, blinks - 1)
    memory[(stone, blinks)] = val
    return val

print(sum(solve(stone, 25) for stone in stones))
print(sum(solve(stone, 75) for stone in stones))
