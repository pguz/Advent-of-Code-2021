# Day 6: Lanternfish
from functools import lru_cache


def parse_file(fd):
    return (list(map(int, fd.readline().split(","))),)


def run_lanternfish_split_80_days(initial_state):
    return sum([_lanternfish_split(80 - s) for s in initial_state])


def run_lanternfish_split_256_days(initial_state):
    return sum([_lanternfish_split(256 - s) for s in initial_state])


@lru_cache
def _lanternfish_split(days):
    if days <= 0:
        return 1
    return _lanternfish_split(days - 7) + _lanternfish_split(days - 9)


solution_function_01 = run_lanternfish_split_80_days
solution_function_02 = run_lanternfish_split_256_days
