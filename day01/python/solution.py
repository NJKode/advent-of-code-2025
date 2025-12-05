import math

def part_one(input):
    start = 50
    current = start

    pw = 0

    for line in input.splitlines():
        direction = line[:1]
        ticks = int(line[1:])
        if ticks > 100:
            ticks = int(line[-2:])

        if direction == "R":
            current += ticks
        else:
            current -= ticks

        if current < 0:
            current = 100 + current

        if current > 99:
            current = current - 100

        if current == 0:
            pw += 1

    return pw


def part_two(input):
    start = 50
    current = start

    pw = 0

    for line in input.splitlines():
        prev = current

        direction = line[:1]
        ticks = int(line[1:])

        if ticks >= 100:
            hundreds = math.floor(ticks / 100)
            pw += hundreds

            ticks = ticks - (hundreds * 100)

        if direction == "R":
            current += ticks
        else:
            current -= ticks

        if current == 0:
            pw += 1
        elif current < 0:
            if prev != 0:
                pw += 1
            current = 100 + current
        elif current > 99:
            if prev != 0:
                pw += 1
            current = current - 100

    return pw

