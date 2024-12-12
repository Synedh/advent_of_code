grid = {(x,y): (val, None) for x, line in enumerate(open('input')) for y, val in enumerate(line.strip())}
areas = []

def get_area(x, y, value, area_id):
    grid[(x, y)] = value, area_id
    area = 1
    perimeter = 4
    neightbours = [(dx, dy) for dx, dy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if (dx, dy) in grid]
    for n_coords in neightbours:
        n_value, n_area_id = grid[n_coords]
        if value == n_value and n_area_id is None:
            n_area, n_perimeter = get_area(n_coords, n_value, area_id)
            area += n_area
            perimeter += n_perimeter
        if value == n_value:
            perimeter -= 1
    return area, perimeter


for coords, (value, area) in grid.items():
    if area is not None:
        continue
    areas.append(get_area(*coords, value, len(areas)))

print(sum(area * perimeter for area, perimeter in areas))
