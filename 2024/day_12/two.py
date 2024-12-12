grid = {(x,y): (val, None) for x, line in enumerate(open('input')) for y, val in enumerate(line.strip())}
areas = []

def get_neightbours(x, y):
    neightbours = []
    p_neightbours = [
        ('^', x - 1, y),
        ('v', x + 1, y),
        ('<', x, y - 1),
        ('>', x, y + 1)
    ]
    for side, dx, dy in p_neightbours:
        if (dx, dy) in grid:
            neightbours.append((side, dx, dy))
    return neightbours

def get_area(x, y, value, area_id):
    neightbours = get_neightbours(x, y)
    grid[(x, y)] = value, area_id
    area = 1
    edges = [('^', x, y), ('v', x, y), ('<', x, y), ('>', x, y)]
    for edge, nx, ny in neightbours:
        n_value, n_area_id = grid[(nx, ny)]
        if value == n_value and n_area_id is None:
            n_area, n_edges = get_area(nx, ny, n_value, area_id)
            area += n_area
            edges += n_edges
        if value == n_value:
            edges.remove((edge, x, y))
    return area, edges

for coords, (value, area) in grid.items():
    if area is not None:
        continue
    area_size, area_edges = get_area(*coords, value, len(areas))
    nb_edges = 0
    for i, (side, x, y) in enumerate(area_edges):
        if (side in ('^', 'v') and (side, x, y - 1) not in area_edges
            or side in ('<', '>') and (side, x - 1, y) not in area_edges):
            nb_edges += 1
    areas.append((area_size, nb_edges))

print(sum(area * nb_edges for area, nb_edges in areas))
