import itertools
import numpy as np
from scipy.optimize import linprog


def get_all_combinations(buttons):
    all_combinations = []
    for b in range(1, len(buttons) + 1):
        all_combinations.extend(itertools.combinations(buttons, b))
    return all_combinations


def flip_lights(lights, button):
    new_lights = [l for l in lights]
    for b in button:
        new_lights[b] = "." if lights[b] == "#" else "#"
    return new_lights


def part_one(input):
    lines = input.splitlines()

    machines = []

    for line in lines:
        lights_start = 1
        lights_end = line.index("]")
        lights = line[lights_start:lights_end].strip()

        buttons_start = lights_end + 1
        buttons_end = line.index("{") - 1

        buttons = line[buttons_start:buttons_end].strip()

        machines.append((lights, buttons))

    total_presses = 0
    for lights, buttons in machines:
        desired_lights = list(lights)

        button_wiring = []
        button_strings = buttons.split(" ")
        for button_string in button_strings:
            number_string = button_string[1:-1]
            numbers = number_string.split(",")
            numbers = [int(n) for n in numbers]
            button_wiring.append(numbers)

        button_combinations = get_all_combinations(button_wiring)

        min_presses = -1
        for combination in button_combinations:
            current_lights = list("." * len(desired_lights))
            num_presses = 0
            for button_press in combination:
                current_lights = flip_lights(current_lights, button_press)

            if current_lights == desired_lights:
                num_presses = len(combination)
                if min_presses == -1 or num_presses < min_presses:
                    min_presses = num_presses
        total_presses += min_presses

    return total_presses


def part_two(input):
    lines = input.splitlines()

    machines = []

    for line in lines:
        lights_end = line.index("]")
        buttons_start = lights_end + 1
        buttons_end = line.index("{") - 1
        configs_start = buttons_end + 2
        configs_end = line.index("}")

        buttons_string = line[buttons_start:buttons_end].strip()
        buttons = buttons_string.split(" ")

        joltages = line[configs_start:configs_end].strip()
        joltages = [int(n) for n in joltages.split(",")]

        machines.append((buttons, joltages))

    result = 0

    for buttons, joltages in machines:
        problem_matrix = []
        for button in buttons:
            schematic_string = button[1:-1]
            schematic = [int(n) for n in schematic_string.split(",")]

            button_array = [0 for i in range(len(joltages))]

            for ind in schematic:
                button_array[ind] = 1

            problem_matrix.append(button_array)

        matrix_np = np.array(problem_matrix)
        A = matrix_np.transpose()
        # becomes
        # [
        #   [0, 0, 0, 0, 1, 1],
        #   [0, 1, 0, 0, 0, 1],
        #   [0, 0, 1, 1, 1, 0],
        #   [1, 1, 0, 1, 0, 0],
        # ]
        c = np.ones(len(buttons))
        desired_joltages = np.array(joltages)
        integrality = np.ones_like(c)  # forces results to be integers

        res = linprog(c, A_eq=A, b_eq=desired_joltages, integrality=integrality)
        result += int(round(res.fun))

    return result
