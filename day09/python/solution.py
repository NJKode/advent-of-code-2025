import shapely
from shapely.geometry.polygon import Polygon


def part_one(input):
    lines = input.splitlines()

    coords = []
    for line in lines:
        coord = line.split(",")
        x = int(coord[0])
        y = int(coord[1])
        coords.append((x, y))

    max_area = 0
    for i_a, tile_a in enumerate(coords):
        for i_b in range(i_a + 1, len(coords)):
            tile_b = coords[i_b]
            area = (abs(tile_b[0] - tile_a[0]) + 1) * (abs(tile_b[1] - tile_a[1]) + 1)
            if area > max_area:
                max_area = area

    return max_area


def part_two(input):
    lines = input.splitlines()

    coords = []
    for line in lines:
        coord = line.split(",")
        x = int(coord[0])
        y = int(coord[1])
        coords.append((x, y))

    max_area = 0
    polygon = Polygon(coords)
    shapely.prepare(polygon)

    for i_a, tile_a in enumerate(coords):
        for i_b in range(i_a + 2, len(coords)):
            if i_a == i_b:
                continue

            tile_b = coords[i_b]
            square_coords = [
                (tile_a[0], tile_a[1]),
                (tile_a[0], tile_b[1]),
                (tile_b[0], tile_b[1]),
                (tile_b[0], tile_a[1]),
            ]

            square = Polygon(square_coords)

            if not polygon.covers(square):
                continue

            area = (abs(tile_b[0] - tile_a[0]) + 1) * (abs(tile_b[1] - tile_a[1]) + 1)
            if area > max_area:
                max_area = area

    return max_area
