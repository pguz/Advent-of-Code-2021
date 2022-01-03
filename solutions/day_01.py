# Day 1: Sonar Sweep


def parse_file(fd):
    return (list(map(int, fd.read().splitlines())),)


def count_depth_increases(measurements):
    return sum([n > p for n, p in zip(measurements[1:], measurements[:-1])])


def count_depth_increases_with_sliding_window(measurements):
    return sum([n > p for n, p in zip(measurements[3:], measurements[:-3])])


solution_function_01 = count_depth_increases
solution_function_02 = count_depth_increases_with_sliding_window
