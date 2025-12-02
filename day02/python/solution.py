import math
import time


input_filepath = "../input/input.txt"


def part_one():
    factors = {
        0: [],
        1: [],
        2: [1],
        3: [],
        4: [2],
        5: [],
        6: [3],
        7: [],
        8: [4],
        9: [],
        10: [5],
    }
    bad_ids = set()

    text_file = open(input_filepath, "r")
    input = text_file.read()
    text_file.close()

    result = 0

    ranges = input.split(",")
    for ids in ranges:
        values = ids.split("-")
        bot = int(values[0])
        top = int(values[1])

        bot_string = str(bot)
        top_string = str(top)
        min_len = len(bot_string)
        max_len = len(top_string)
        id_lengths = list(range(min_len, max_len + 1))

        possible_lengths = list(set(factors[min_len] + factors[max_len]))
        possible_lengths.sort()

        # get all 1-digit numbers between 1-9
        # get all 2-digit numbers between 12-98
        # get all 5-digit numbers between 12345-98765
        test_nums = []

        for index, num_chars in enumerate(possible_lengths):
            min_pattern = bot_string[:num_chars]
            # min_num = int(min_pattern)
            min_num = int(math.pow(10, num_chars - 1))

            max_pattern = top_string[:num_chars]
            # max_num = int(max_pattern)
            max_num = int(math.pow(10, num_chars))

            possible_range = list(range(min_num, max_num))
            test_nums += possible_range

        for t in test_nums:
            for l in id_lengths:
                # num_repeats = int(l / len(str(t)))
                num_repeats = 2
                new_num_string = str(t) * num_repeats
                new_num = int(new_num_string)

                if new_num >= bot and new_num <= top:
                    bad_ids.add(new_num)

    for id in bad_ids:
        result += id
    print(result)


def part_two():
    start = time.time()

    factors = {
        0: [],
        1: [],
        2: [1],
        3: [1],
        4: [1, 2],
        5: [1],
        6: [1, 2, 3],
        7: [1],
        8: [1, 2, 4],
        9: [1, 3],
        10: [1, 2, 5],
    }

    bad_ids = set()

    text_file = open(input_filepath, "r")
    input = text_file.read()
    text_file.close()

    result = 0

    ranges = input.split(",")
    for ids in ranges:
        values = ids.split("-")
        bot = int(values[0])
        top = int(values[1])

        bot_string = str(bot)
        top_string = str(top)
        min_len = len(bot_string)
        max_len = len(top_string)
        id_lengths = list(range(min_len, max_len + 1))

        possible_lengths = list(set(factors[min_len] + factors[max_len]))
        possible_lengths.sort()

        # 1234567890-9876543210
        # get all 1-digit numbers between 1-9
        # get all 2-digit numbers between 12-98
        # get all 5-digit numbers between 12345-98765
        test_nums = []

        for index, num_chars in enumerate(possible_lengths):
            min_pattern = bot_string[:num_chars]
            # min_num = int(min_pattern)
            min_num = int(math.pow(10, num_chars - 1))

            max_pattern = top_string[:num_chars]
            # max_num = int(max_pattern)
            max_num = int(math.pow(10, num_chars))

            possible_range = list(range(min_num, max_num + 1))
            test_nums += possible_range

        for t in test_nums:
            for l in id_lengths:
                if l <= len(str(t)):
                    continue
                num_repeats = int(l / len(str(t)))
                new_num_string = str(t) * num_repeats
                new_num = int(new_num_string)

                if new_num >= bot and new_num <= top:
                    bad_ids.add(new_num)

    for id in bad_ids:
        result += id
    end = time.time()
    print((end - start) * 1000)

    print(result)


if __name__ == "__main__":
    part_two()
