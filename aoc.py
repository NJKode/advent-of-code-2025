import click
import time

import day01.python.solution as day01
import day02.python.solution as day02
import day03.python.solution as day03

solutions = {
    (1, 1): day01.part_one,
    (1, 2): day01.part_two,
    (2, 1): day02.part_one,
    (2, 2): day02.part_two,
    (3, 1): day03.part_one,
    (3, 2): day03.part_two,
    # (4, 1): day04.part_one,
    # (4, 2): day04.part_two,
    # (5, 1): day05.part_one,
    # (5, 2): day05.part_two,

}


@click.command()
@click.argument('day')
@click.argument('part')
@click.option('-t', '--test', is_flag=True,
              help='Run the test.txt file')
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
    solution(input)
    end = time.time()

    elapsed_seconds = end - start
    print("-------")
    print(f"Completed in {elapsed_seconds} seconds.")

if __name__ == '__main__':
    runner()