

def part_one(input):
    lines = input.splitlines()

    num_fresh_ingredients = 0
    id_ranges = set()
    blank_line_index = -1

    for index, line in enumerate(lines):
        if line == "":
            blank_line_index = index
            break

        id_range_limits = line.split("-")
        lower = int(id_range_limits[0])
        upper = int(id_range_limits[1])

        id_ranges.add((lower, upper))


    ingredient_ids = lines[blank_line_index + 1:]
    for id in ingredient_ids:
        id = int(id)
        for lower_limit, upper_limit in id_ranges:
            if id >= lower_limit and id <= upper_limit:
                num_fresh_ingredients += 1
                break

    print(num_fresh_ingredients)


def part_two(input):
    lines = input.splitlines()

    num_fresh_ingredients = 0

    id_ranges = set()

    for line in lines:
        if line == "":
            break

        id_range_limits = line.split("-")
        lower = int(id_range_limits[0])
        upper = int(id_range_limits[1])

        id_ranges.add((lower, upper))

    sorted_ranges = sorted(id_ranges, key=lambda x: x[0])
    # sort ranges lowest-to-highest based on lower limit of range

    start_range = sorted_ranges[0]
    current_lower_limit, current_upper_limit = start_range
    for id_range in sorted_ranges:
        lower_limit, upper_limit = id_range

        if lower_limit <= current_upper_limit and upper_limit > current_upper_limit:
            current_upper_limit = upper_limit
        elif lower_limit > current_upper_limit:
            num_fresh_ingredients += (1 + current_upper_limit - current_lower_limit)
            current_lower_limit = lower_limit
            current_upper_limit = upper_limit

    num_fresh_ingredients += (1 + current_upper_limit - current_lower_limit)

    print(num_fresh_ingredients)






