import click
import time

import day01.python.solution as day01
import day02.python.solution as day02
import day03.python.solution as day03
import day04.python.solution as day04
import day05.python.solution as day05
import day06.python.solution as day06
import day07.python.solution as day07
import day08.python.solution as day08
import day09.python.solution as day09
import day10.python.solution as day10
import day11.python.solution as day11
import day12.python.solution as day12


solutions = {
    (1, 1): day01.part_one,
    (1, 2): day01.part_two,
    (2, 1): day02.part_one,
    (2, 2): day02.part_two,
    (3, 1): day03.part_one,
    (3, 2): day03.part_two,
    (4, 1): day04.part_one,
    (4, 2): day04.part_two,
    (5, 1): day05.part_one,
    (5, 2): day05.part_two,
    (6, 1): day06.part_one,
    (6, 2): day06.part_two,
    (7, 1): day07.part_one,
    (7, 2): day07.part_two,
    (8, 1): day08.part_one,
    (8, 2): day08.part_two,
    (9, 1): day09.part_one,
    (9, 2): day09.part_two,
    (10, 1): day10.part_one,
    (10, 2): day10.part_two,
    (11, 1): day11.part_one,
    (11, 2): day11.part_two,
    (12, 1): day12.part_one,
    (12, 2): day12.part_two,
}


@click.command()
@click.argument("day")
@click.argument("part")
@click.option("-t", "--test", is_flag=True, help="Run the test.txt file")
def runner(day, part, test):
    day = int(day)
    part = int(part)
    assert day >= 1 and day <= 12, f"'{day}' is not a valid number between 1-12."

    day_string = str(day)
    if day < 10:
        day_string = "0" + day_string
    filename = "test" if test else "input"

    input_filepath = f"day{day_string}/input/{filename}.txt"
    text_file = open(input_filepath, "r")
    input = text_file.read()
    text_file.close()

    solution = solutions[(day, part)]

    start = time.time()
    answer = solution(input)

    print("-------")
    if answer == -1:
        print(f"Solution for day {day_string} not yet completed.")
    else:
        print(answer)
    print("-------")

    end = time.time()
    elapsed_seconds = end - start
    print(f"Completed in {elapsed_seconds} seconds.")


if __name__ == "__main__":
    runner()
