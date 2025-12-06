import math


def part_one(input):
    lines = input.splitlines()

    grid = [line.split() for line in lines]
    result = 0
    for op in range(0, len(grid[0])):
        operands = []
        for eq in range(0, len(grid)):
            operands.append(grid[eq][op])

        operation = operands.pop()
        operands = [int(op) for op in operands]
        if operation == "+":
            result += sum(operands)
        elif operation == "*":
            result += math.prod(operands)

    return result


def part_two(input):
    lines = input.splitlines()

    num_rows = len(lines)
    num_columns = len(lines[0])
    grid = []
    for col in range(num_columns - 1, -1, -1):
        # step backwards from rightmost column
        vals = []
        for row in range(0, num_rows):
            vals.append(lines[row][col])
        grid.append(vals)

    result = 0

    operands = []
    for exploded_operand in grid:
        operator = exploded_operand[-1]
        if operator == "+" or operator == "*":
            exploded_operand = exploded_operand[:-1]
        else:
            operator = ""

        operand_string = "".join(exploded_operand).strip()
        if operand_string == "":
            continue

        operand = int("".join(exploded_operand))
        operands.append(operand)

        if operator == "":
            continue

        if operator == "+":
            result += sum(operands)
        elif operator == "*":
            result += math.prod(operands)

        operands = []

    return result
