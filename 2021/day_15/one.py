input = '1163751742\n1381373672\n2136511328\n3694931569\n7463417111\n1319128137\n1359912421\n3125421639\n1293138521\n2311944581\n'
cave = [[int(value) for value in line] for line in open('input').read().splitlines()]
lenX, lenY = len(cave), len(cave[0])

def dijkstra():
    dist = [[float('inf') for _ in range(lenY)] for _ in range(lenX)]
    prev = [[None for _ in range(lenY)] for _ in range(lenX)]
    Q = set((x, y) for y in range(lenY) for x in range(lenX))
    adj = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    dist[0][0] = 0

    while len(Q):
        x, y = min((((x, y), dist[x][y]) for y in range(lenY) for x in range(lenX) if (x, y) in Q), key=lambda value: value[1])[0]
        Q.remove((x, y))

        for x1, y1 in [(x + dx, y + dy) for dx, dy in adj if (x + dx, y + dy) in Q]:
            alt = dist[x][y] + cave[x1][y1]
            if alt < dist[x1][y1]:
                dist[x1][y1] = alt
                prev[x1][y1] = (x, y)

    return dist[-1][-1]


print(dijkstra())
