
def part_one(input):

    banks = input.splitlines()

    result = 0
    for bank in banks:
        numbers = [int(n) for n in bank]
        sorted_numbers = [int(n) for n in bank]
        sorted_numbers.sort()

        max_num = -1

        max_num_index = len(numbers) - 1
        while max_num_index == len(numbers) - 1:
            max_num = sorted_numbers.pop()
            max_num_index = numbers.index(max_num)


        remaining_numbers = numbers[max_num_index+1:]
        remaining_numbers.sort()
        second_num = remaining_numbers[-1:][0]

        num_string = str(max_num) + str(second_num)
        joltage = int(num_string)
        result += joltage

    print(result)



def part_two(input):
    banks = input.splitlines()
    result = 0

    for bank in banks:
        batteries = []

        num_remaining_batteries = 12
        numbers = [int(n) for n in bank]

        while num_remaining_batteries > 0:
            sorted_numbers = [n for n in numbers]
            sorted_numbers.sort()

            max_num_index = len(numbers)
            while max_num_index >= (len(numbers) - num_remaining_batteries + 1) and len(sorted_numbers) > 0:
                max_num = sorted_numbers.pop()
                max_num_index = numbers.index(max_num)

            batteries.append(max_num)
            numbers = numbers[max_num_index+1:]
            num_remaining_batteries -= 1

        joltage_string = ""
        for b in batteries:
            joltage_string += str(b)

        joltage = int(joltage_string)
        result += joltage

    print(result)