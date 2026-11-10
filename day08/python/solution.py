import math
from collections import Counter

def straight_distance(coord_a, coord_b):
    x_1, y_1, z_1 = coord_a
    x_2, y_2, z_2 = coord_b

    return math.sqrt(
        math.pow(x_1 - x_2, 2)
        + math.pow(y_1 - y_2, 2)
        + math.pow(z_1 - z_2, 2)
    )


def find_closest_neighbours(coords, seen_neighbours):
    neighbours = {}
    # print(coords)

    smallest_distance = -1
    closest_neighbours = ()
    for index_a, coord_a in enumerate(coords):
        min_distance = -1
        closest_neighbour = (-1, -1, -1)
        for index_b, coord_b in enumerate(coords):
            if index_a == index_b:
                continue

            if (coord_a, coord_b) in seen_neighbours:
                continue

            distance = straight_distance(coord_a, coord_b)

            if min_distance == -1 or distance < min_distance:
                min_distance = distance
                closest_neighbour = coord_b

        if smallest_distance == -1 or min_distance < smallest_distance:
            smallest_distance = min_distance
            closest_neighbours = (coord_a, closest_neighbour, smallest_distance)

        neighbours[coord_a] = (distance, closest_neighbour)

    return closest_neighbours


def part_one(input):
    lines = input.splitlines()
    box_coords = []
    for line in lines:
        coords = line.split(",")
        box_coords.append((int(coords[0]), int(coords[1]), int(coords[2])))

    box_coords = set(box_coords)

    num_iterations = 1000

    current_circuit_id = 0
    circuit_ids = {}
    seen_neighbours = set()
    for i in range(0, num_iterations):
        neighbour_a, neighbour_b, _distance = find_closest_neighbours(box_coords, seen_neighbours)
        seen_neighbours.add((neighbour_b, neighbour_a))

        if neighbour_a in circuit_ids and neighbour_b in circuit_ids:
            if circuit_ids[neighbour_a] == circuit_ids[neighbour_b]:
                continue
            else:
                circuits_to_change = [key for key, value in circuit_ids.items() if value == circuit_ids[neighbour_b]]
                for circuit in circuits_to_change:
                    circuit_ids[circuit] = circuit_ids[neighbour_a]
        elif neighbour_a in circuit_ids:
            circuit_ids[neighbour_b] = circuit_ids[neighbour_a]
        elif neighbour_b in circuit_ids:
            circuit_ids[neighbour_a] = circuit_ids[neighbour_b]
        else:
            current_circuit_id += 1
            circuit_ids[neighbour_a] = current_circuit_id
            circuit_ids[neighbour_b] = current_circuit_id

    circuit_lengths = list(Counter(circuit_ids.values()).values())
    circuit_lengths.sort()
    result = math.prod(circuit_lengths[-3:])

    return result


def get_distance_between_boxes(coords):
    distances = {}

    for index_a, coord_a in enumerate(coords):
        for index_b in range(index_a + 1, len(coords)):
            coord_b = coords[index_b]

            distance = straight_distance(coord_a, coord_b)
            distances[(coord_a, coord_b)] = distance

    return distances


def part_two(input):
    lines = input.splitlines()
    box_coords = []
    for line in lines:
        coords = line.split(",")
        box_coords.append((int(coords[0]), int(coords[1]), int(coords[2])))

    box_distances = get_distance_between_boxes(box_coords)
    sorted_box_distances = sorted(box_distances.items(), key=lambda item: item[1])

    circuit_ids = {}
    current_circuit_id = 0
    connected_boxes = []
    for (neighbour_a, neighbour_b), distance in sorted_box_distances:
        if neighbour_a in circuit_ids and neighbour_b in circuit_ids:
            if circuit_ids[neighbour_a] == circuit_ids[neighbour_b]:
                continue
            else:
                circuits_to_change = [key for key, value in circuit_ids.items() if value == circuit_ids[neighbour_b]]
                for circuit in circuits_to_change:
                    circuit_ids[circuit] = circuit_ids[neighbour_a]
        elif neighbour_a in circuit_ids:
            circuit_ids[neighbour_b] = circuit_ids[neighbour_a]
        elif neighbour_b in circuit_ids:
            circuit_ids[neighbour_a] = circuit_ids[neighbour_b]
        else:
            current_circuit_id += 1
            circuit_ids[neighbour_a] = current_circuit_id
            circuit_ids[neighbour_b] = current_circuit_id

        num_ids = set(circuit_ids.values())
        if len(num_ids) == 1:
            connected_boxes = [neighbour_a, neighbour_b]

    result = connected_boxes[0][0] * connected_boxes[1][0]
    return result
