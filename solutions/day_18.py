# Day 18: Snailfish
import copy


def parse_file(fd):
    snailfishes = []
    for line in fd.read().splitlines():
        level = 0
        snailfish = []
        for c in line:
            if c == "[":
                level += 1
            elif c == "]":
                level -= 1
            elif c == ",":
                pass
            else:
                snailfish.append([level, int(c)])
        snailfishes.append(snailfish)
    return (snailfishes,)


def _add_snailfishes(snailfish, snailfish_to_add):

    for i in range(len(snailfish)):
        snailfish[i][0] += 1
    for i in range(len(snailfish_to_add)):
        snailfish_to_add[i][0] += 1

    snailfish.extend(snailfish_to_add)

    stable = False
    while stable is False:
        stable = True
        for i in range(len(snailfish)):
            if snailfish[i][0] > 4:
                if i > 0:
                    snailfish[i - 1][1] += snailfish[i][1]
                if i < len(snailfish) - 2:
                    snailfish[i + 2][1] += snailfish[i + 1][1]
                snailfish[i] = [snailfish[i][0] - 1, 0]
                snailfish.pop(i + 1)
                stable = False
                break

        if stable is False:
            continue

        for i, (l, v) in enumerate(snailfish):
            if v >= 10:
                snailfish[i] = [l + 1, v // 2]
                snailfish.insert(i + 1, [l + 1, v // 2 + v % 2])
                stable = False
                break

    return snailfish


def _find_magnitude(snailfish):
    while len(snailfish) != 1:
        i = 0
        while True:
            if snailfish[i][0] == snailfish[i + 1][0]:
                snailfish[i] = [
                    snailfish[i][0] - 1,
                    3 * snailfish[i][1] + 2 * snailfish[i + 1][1],
                ]
                snailfish.pop(i + 1)
                break
            i += 1
    return snailfish[0][1]


def process_snailfishes(snailfishes):

    snailfish = snailfishes[0]
    for snailfish_to_add in snailfishes[1:]:
        _add_snailfishes(snailfish, snailfish_to_add)

    return _find_magnitude(snailfish)


def find_the_biggest_magnitude(snailfishes):

    max_magnitude = 0
    for i in range(len(snailfishes)):
        for j in range(len(snailfishes)):
            if i == j:
                continue
            snailfish_1 = copy.deepcopy(snailfishes[i])
            snailfish_2 = copy.deepcopy(snailfishes[j])
            magnitude = _find_magnitude(_add_snailfishes(snailfish_1, snailfish_2))
            if magnitude > max_magnitude:
                max_magnitude = magnitude

    return max_magnitude


solution_function_01 = process_snailfishes
solution_function_02 = find_the_biggest_magnitude
