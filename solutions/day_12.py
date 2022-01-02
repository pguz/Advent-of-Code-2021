# Day 12: Passage Pathing
from collections import defaultdict


def parse_file(fd):
    return ([tuple(line.split("-")) for line in fd.read().splitlines()],)


def find_paths_small_once(caves_connections):
    edges = defaultdict(list)

    for b, e in caves_connections:
        if e != "start" and b != "end":
            edges[b].append(e)
        if b != "start" and e != "end":
            edges[e].append(b)

    def _dfs(cave, small_caves_visited):
        if cave == "end":
            return 1
        if cave != "start" and cave.islower():
            if cave in small_caves_visited:
                return 0
            small_caves_visited.add(cave)

        return sum([_dfs(v, small_caves_visited.copy()) for v in edges[cave]])

    return _dfs("start", small_caves_visited=set())


def find_paths_one_small_twice(caves_connections):
    edges = defaultdict(list)

    for b, e in caves_connections:
        if e != "start" and b != "end":
            edges[b].append(e)
        if b != "start" and e != "end":
            edges[e].append(b)

    def _dfs(cave, small_caves_visited, small_cave_visited_twice):
        if cave == "end":
            return 1
        if cave != "start" and cave.islower():
            if cave in small_caves_visited:
                if small_cave_visited_twice is False:
                    small_cave_visited_twice = True
                else:
                    return 0
            else:
                small_caves_visited.add(cave)

        return sum(
            [
                _dfs(v, small_caves_visited.copy(), small_cave_visited_twice)
                for v in edges[cave]
            ]
        )

    return _dfs("start", small_caves_visited=set(), small_cave_visited_twice=False)


solution_function_01 = find_paths_small_once
solution_function_02 = find_paths_one_small_twice
