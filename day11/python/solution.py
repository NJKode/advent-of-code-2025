from functools import cache


def part_one(input):
    lines = input.splitlines()

    wiring = {}
    for line in lines:
        servers = line.split()

        server_from = servers[0][:-1]
        wiring[server_from] = servers[1:]

    result = dfs_recursive(wiring, "you")

    return result


def dfs_recursive(wiring, device):
    if device == "out":
        return 1

    val = 0
    for output in wiring[device]:
        val += dfs_recursive(wiring, output)
    return val


wiring_p2: dict[str, list[str]] = {}


def part_two(input):
    lines = input.splitlines()

    for line in lines:
        servers = line.split()

        server_from = servers[0][:-1]
        wiring_p2[server_from] = servers[1:]

    result = dfs_part_two("svr")
    return result


@cache
def dfs_part_two(device, seen_fft=False, seen_dac=False):
    if device == "out":
        return 1 if seen_fft and seen_dac else 0
    seen_fft = seen_fft or device == "fft"
    seen_dac = seen_dac or device == "dac"

    val = 0
    for output in wiring_p2[device]:
        val += dfs_part_two(output, seen_fft, seen_dac)
    return val
