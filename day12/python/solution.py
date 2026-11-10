import numpy as np

def check_validity(tree_dimensions, required_presents, present_shapes):
    tree_x, tree_y = tree_dimensions
    available_space = tree_x * tree_y

    total_space = 0
    for i, rp in enumerate(required_presents):
        present = present_shapes[i]
        total_space += (rp* np.sum(present))

    if available_space < total_space:
        return False

    return True

def part_one(input):
    lines = input.splitlines()
    shape_boundaries = [1, 6, 11, 16, 21, 26]
    trees_start = 30

    shapes = []
    for b in shape_boundaries:
        shape = []
        for i in range(b, b+3):
            row = []
            for space in list(lines[i]):
                row.append(1 if space == "#" else 0)
            shape.append(row)
        shapes.append(shape)

    shapes_np = [np.array(shape) for shape in shapes]

    trees = []
    for l in range(trees_start, len(lines)):
        line = lines[l]
        parts = line.split(":")
        dimensions = parts[0].split("x")
        num_presents = [int(n) for n in parts[1].strip().split()]
        trees.append(((int(dimensions[0]), int(dimensions[1])), num_presents))


    num_valid = 0

    for dim, num_pres in trees:
        is_valid = check_validity(dim, num_pres, shapes_np)
        if (is_valid):
            print(dim)
        num_valid += 1 if is_valid else 0

    return num_valid


def part_two(input):
    result = -1

    return result


