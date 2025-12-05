

def part_one(input):
    num_accessible_rolls = 0

    rows = input.splitlines()

    map_space = [list(row) for row in rows]
    height = len(map_space)
    width = len(map_space[0])

    for y, row in enumerate(map_space):
        for x, space in enumerate(row):
            adjacent_count = 0
            if space == '.':
                continue

            if space == '@':
                # check up
                if y > 0 and map_space[y-1][x] == '@':
                    adjacent_count += 1

                # check up right
                if y > 0 and x + 1 < width and map_space[y-1][x+1] == '@':
                    adjacent_count += 1

                if x + 1 < width and map_space[y][x+1] == '@':
                    adjacent_count += 1

                if x+1 < width and y+1 < height and map_space[y+1][x+1] == '@':
                    adjacent_count += 1

                if y + 1 < height and map_space[y+1][x] == '@':
                    adjacent_count += 1

                if y + 1 < height and x > 0 and map_space[y+1][x-1] == '@':
                    adjacent_count += 1

                if x > 0 and map_space[y][x-1] == '@':
                    adjacent_count += 1

                if x > 0 and y > 0 and map_space[y-1][x-1] == '@':
                    adjacent_count += 1

                if adjacent_count < 4:
                    num_accessible_rolls += 1

    return num_accessible_rolls


def part_two(input):
    rows = input.splitlines()
    map_space = [list(row) for row in rows]

    num_accessible_rolls = 1 # will be overwritten in loop below
    rolls_removed = 0

    while num_accessible_rolls > 0:
        accessible_rolls = _get_accessible_rolls(map_space)
        num_accessible_rolls = len(accessible_rolls)

        for x, y in accessible_rolls:
            map_space[y][x] = '.'

        rolls_removed += num_accessible_rolls

    return rolls_removed


def _get_accessible_rolls(map_space):
    height = len(map_space)
    width = len(map_space[0])

    accessible_rolls = set()

    for y, row in enumerate(map_space):
        for x, space in enumerate(row):
            adjacent_count = 0
            if space == '.':
                continue

            if space == '@':
                # up
                if y > 0 and map_space[y-1][x] == '@':
                    adjacent_count += 1

                # up right
                if y > 0 and x + 1 < width and map_space[y-1][x+1] == '@':
                    adjacent_count += 1

                # right
                if x + 1 < width and map_space[y][x+1] == '@':
                    adjacent_count += 1

                # down right
                if x+1 < width and y+1 < height and map_space[y+1][x+1] == '@':
                    adjacent_count += 1

                # down
                if y + 1 < height and map_space[y+1][x] == '@':
                    adjacent_count += 1

                # down left
                if y + 1 < height and x > 0 and map_space[y+1][x-1] == '@':
                    adjacent_count += 1

                # left
                if x > 0 and map_space[y][x-1] == '@':
                    adjacent_count += 1

                # up left
                if x > 0 and y > 0 and map_space[y-1][x-1] == '@':
                    adjacent_count += 1

            if adjacent_count < 4:
                accessible_rolls.add((x, y))

    return accessible_rolls
