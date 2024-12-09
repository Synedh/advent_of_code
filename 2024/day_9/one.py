diskmap = map(int, list(open('input').readline()[:-1]))

id = 0
disk = []
for i, size in enumerate(diskmap):
    if not i % 2:
        disk += [id] * size
        id += 1
    else:
        disk += [None] * size

i = 0
while i < len(disk):
    if disk[i] is None:
        disk[i], disk[-1] = disk[-1], disk[i]
        while disk[-1] is None:
            disk.pop()
    i += 1
print(sum(i * val for i, val in enumerate(disk)))
