# Day 5: Hydrothermal Venture
from collections import defaultdict


def parse_file(fd):
    vents = []
    for line in fd.read().splitlines():
        points = line.split(" -> ")
        fp = tuple(map(int, points[0].split(",")))
        sp = tuple(map(int, points[1].split(",")))
        fp, sp = (
            (fp, sp)
            if ((fp[0] < sp[0]) or (fp[0] == sp[0] and fp[1] < sp[1]))
            else (sp, fp)
        )
        vents.append((fp, sp))
    return (vents,)


def detect_vents_simple(vents):
    vents_points = defaultdict(int)
    for vent in vents:
        if vent[0][0] == vent[1][0]:
            for c in range(vent[0][1], vent[1][1] + 1):
                vents_points[(vent[0][0], c)] += 1
            continue
        if vent[0][1] == vent[1][1]:
            for c in range(vent[0][0], vent[1][0] + 1):
                vents_points[(c, vent[0][1])] += 1
            continue
    return sum([v >= 2 for v in vents_points.values()])


def detect_vents_with_diag(vents):
    vents_points = defaultdict(int)
    for vent in vents:
        if vent[0][0] == vent[1][0]:
            for p in range(vent[0][1], vent[1][1] + 1):
                vents_points[(vent[0][0], p)] += 1
            continue
        if vent[0][1] == vent[1][1]:
            for p in range(vent[0][0], vent[1][0] + 1):
                vents_points[p, vent[0][1]] += 1
            continue
        if vent[1][1] - vent[0][1] == vent[1][0] - vent[0][0]:
            for p in range(0, vent[1][1] - vent[0][1] + 1):
                vents_points[vent[0][0] + p, vent[0][1] + p] += 1
            continue
        if vent[0][1] - vent[1][1] == vent[1][0] - vent[0][0]:
            for p in range(0, vent[1][0] - vent[0][0] + 1):
                vents_points[vent[0][0] + p, vent[0][1] - p] += 1
            continue
    return sum([v >= 2 for v in vents_points.values()])


solution_function_01 = detect_vents_simple
solution_function_02 = detect_vents_with_diag
