diskmap = map(int, list(open('input').readline()[:-1]))

id = 0
disk = []
for i, size in enumerate(diskmap):
    if not i % 2:
        disk += [id] * size
        id += 1
    else:
        disk += [None] * size

i = len(disk) -1
while i > 0:
    print(f'\r{len(disk) - i}/{len(disk)}', end='')
    id = disk[i]
    size = 1
    while disk[i - size] == id:
        size += 1
    if id is not None:
        for j in range(len(disk[:i])):
            if disk[j:j + size] == [None] * size:
                disk[j:j + size] = [id] * size
                disk[i - size + 1:i + 1] = [None] * size
                break
    i -= size
print()
print(sum(i * val for i, val in enumerate(disk) if val))
