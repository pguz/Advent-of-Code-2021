# Day 14: Extended Polymerization
from collections import Counter
from functools import lru_cache


def parse_file(fd):
    lines = fd.read().splitlines()
    template = lines.pop(0)
    rules = dict()
    for line in lines[1:]:
        elements, result = line.split("->")
        rules[(elements[0], elements[1])] = result[1]
    return template, rules


def calculate_polymer_value(template, rules, iterations):
    @lru_cache(maxsize=None)
    def _process(f, s, i):
        if i == 0:
            return Counter()
        m = rules.get((f, s))
        if m is not None:
            return _process(f, m, i - 1) + Counter(m) + _process(m, s, i - 1)

    elements_counter = Counter(template)
    for e1, e2 in zip(template[:-1], template[1:]):
        elements_counter += _process(e1, e2, iterations)

    most_common_elements = elements_counter.most_common()
    return most_common_elements[0][1] - most_common_elements[-1][1]


def calculate_polymer_value_10_iters(template, rules):
    return calculate_polymer_value(template, rules, iterations=10)


def calculate_polymer_value_40_iters(template, rules):
    return calculate_polymer_value(template, rules, iterations=40)


solution_function_01 = calculate_polymer_value_10_iters
solution_function_02 = calculate_polymer_value_40_iters
