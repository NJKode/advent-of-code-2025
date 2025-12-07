import copy
from collections import defaultdict


def part_one(input):
    lines = input.splitlines()

    height = len(lines)
    # width = len(lines[0])

    splitter_positions = _get_splitter_positions(lines)

    start_x = lines[0].index("S")

    beam_positions = [start_x]

    num_splits = 0

    for y in range(0, height):
        new_positions = [x for x in beam_positions]
        splitters_on_line = splitter_positions[y]
        split_positions = [x for x in new_positions]
        for index, position in enumerate(new_positions):
            if position in splitters_on_line:
                num_splits += 1
                split_positions[index] = -1
                split_positions.append(position - 1)
                split_positions.append(position + 1)

        split_positions = [x for x in split_positions if x != -1]
        beam_positions = list(set(split_positions))

    return num_splits


def part_two(input):
    lines = input.splitlines()

    height = len(lines)
    # width = len(lines[0])

    splitter_positions = _get_splitter_positions(lines)

    start_x = lines[0].index("S")

    beam_timelines = {start_x: 1}

    for y in range(0, height):
        split_timelines = defaultdict(int, copy.deepcopy(beam_timelines))
        splitters_on_line = splitter_positions[y]

        for position, num_timelines in beam_timelines.items():
            if position in splitters_on_line:
                del split_timelines[position]

                split_timelines[position - 1] += num_timelines
                split_timelines[position + 1] += num_timelines

        beam_timelines = {}
        for position, num_timelines in split_timelines.items():
            beam_timelines[position] = num_timelines

    result = sum(beam_timelines.values())
    return result


def _get_splitter_positions(lines):
    positions = []
    for line in lines:
        splitters_on_line = [x for x, space in enumerate(line) if space == "^"]
        positions.append(splitters_on_line)
    return positions


def _print_manifold_row(width, beam_timelines, splitters_on_line):
    manifold = list("." * width)
    for x in splitters_on_line:
        manifold[x] = "^"
    for x, t in beam_timelines.items():
        manifold[x] = str(t)

    print("".join(manifold))
