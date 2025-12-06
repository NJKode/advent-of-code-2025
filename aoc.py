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

    day_module = globals()[f"day{day_string}"]
    if part == 1:
        solution = day_module.part_one
    elif part == 2:
        solution = day_module.part_two

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
