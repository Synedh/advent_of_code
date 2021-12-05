input = [([*map(int, val.split(' -> ')[0].split(','))], [*map(int, val.split(' -> ')[1].split(','))]) for val in open('input').read().splitlines()]
input = [val for val in input if val[0][0] == val[1][0] or val[0][1] == val[1][1]]

clouds = []
for val in input:
    if val[0][1] == val[1][1]:
        clouds.append({(x, val[0][1]) for x in range(min(val[0][0], val[1][0]), max(val[0][0], val[1][0]) + 1)})
    else:
        clouds.append({(val[0][0], y) for y in range(min(val[0][1], val[1][1]), max(val[0][1], val[1][1]) + 1)})

sames = set()
for cloud1 in clouds:
    for cloud2 in clouds:
        if cloud1 != cloud2:   
            sames = sames.union(cloud1 & cloud2)
print(len(sames))
