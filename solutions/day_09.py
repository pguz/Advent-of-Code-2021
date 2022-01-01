# Day 9: Smoke Basin


def parse_file(fd):
    return (list(fd.read().splitlines()),)


def calculate_sum_of_risk_levels(cave):
    h = len(cave)
    w = len(cave[0])
    risk_level_sum = 0
    for i in range(w):
        for j in range(h):
            cand = cave[j][i]
            if i > 0 and cave[j][i - 1] <= cand:
                continue
            if i < w - 1 and cave[j][i + 1] <= cand:
                continue
            if j > 0 and cave[j - 1][i] <= cand:
                continue
            if j < h - 1 and cave[j + 1][i] <= cand:
                continue
            risk_level_sum += int(cand) + 1
    return risk_level_sum


def calculate_sum_of_risk_levels_v2(cave):
    h = len(cave)
    w = len(cave[0])
    risk_level_sum = 0
    visited = [[False for i in range(w)] for j in range(h)]

    def _find_low_point(j, i):
        if visited[j][i] is True:
            return None
        visited[j][i] = True
        cand = cave[j][i]
        if i > 0:
            if cave[j][i - 1] > cand:
                visited[j][i - 1] = True
            else:
                return _find_low_point(j, i - 1)
        if i < w - 1:
            if cave[j][i + 1] > cand:
                visited[j][i + 1] = True
            else:
                return _find_low_point(j, i + 1)
        if j > 0:
            if cave[j - 1][i] > cand:
                visited[j - 1][i] = True
            else:
                return _find_low_point(j - 1, i)
        if j < h - 1:
            if cave[j + 1][i] > cand:
                visited[j + 1][i] = True
            else:
                return _find_low_point(j + 1, i)
        return cand

    for j in range(h):
        for i in range(w):
            if visited[j][i] is True:
                continue
            potential_low_point = _find_low_point(j, i)
            if potential_low_point is not None:
                risk_level_sum += int(potential_low_point) + 1
    return risk_level_sum


def find_result_from_basins(cave):
    h = len(cave)
    w = len(cave[0])
    visited = [[False for i in range(w)] for j in range(h)]

    def _find_basin(_w, _h):
        if _w < 0 or _w >= w:
            return 0
        if _h < 0 or _h >= h:
            return 0
        if visited[_h][_w] is True:
            return 0
        visited[_h][_w] = True
        if cave[_h][_w] == "9":
            return 0
        return (
            1
            + _find_basin(_w - 1, _h)
            + _find_basin(_w + 1, _h)
            + _find_basin(_w, _h - 1)
            + _find_basin(_w, _h + 1)
        )

    basins = []
    for i in range(w):
        for j in range(h):
            if cave[j][i] == "9":
                continue
            if visited[j][i] is True:
                continue
            basins.append(_find_basin(i, j))
    largest_basins = sorted(basins, reverse=True)[:3]
    return largest_basins[0] * largest_basins[1] * largest_basins[2]


solution_function_01 = calculate_sum_of_risk_levels
solution_function_02 = find_result_from_basins
