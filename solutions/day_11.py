# Day 11: Dumbo Octopus


def parse_file(fd):
    return ([list(map(int, line)) for line in fd.read().splitlines()],)


def find_number_of_flashes_after_100_steps(energy_levels):
    h = len(energy_levels)
    w = len(energy_levels[0])
    flashes_number = 0

    def _add_energy(_h, _w):
        if _w < 0 or _w >= w:
            return
        if _h < 0 or _h >= h:
            return
        if energy_levels[_h][_w] == 0:
            return
        energy_levels[_h][_w] += 1
        if energy_levels[_h][_w] >= 10:
            return True
        else:
            return False

    flashes = set()
    for _ in range(100):
        for i in range(h):
            for j in range(w):
                energy_levels[i][j] += 1
                if energy_levels[i][j] >= 10:
                    flashes.add((i, j))

        while flashes:
            i, j = flashes.pop()
            flashes_number += 1
            energy_levels[i][j] = 0
            for _i, _j in [
                (i - 1, j),
                (i - 1, j + 1),
                (i, j + 1),
                (i + 1, j + 1),
                (i + 1, j),
                (i + 1, j - 1),
                (i, j - 1),
                (i - 1, j - 1),
            ]:
                if _add_energy(_i, _j) is True:
                    flashes.add((_i, _j))

    return flashes_number


def find_all_octopuses_flash_step(energy_levels):
    h = len(energy_levels)
    w = len(energy_levels[0])
    step = 0

    def _add_energy(_h, _w):
        if _w < 0 or _w >= w:
            return
        if _h < 0 or _h >= h:
            return
        if energy_levels[_h][_w] == 0:
            return
        energy_levels[_h][_w] += 1
        if energy_levels[_h][_w] >= 10:
            return True
        else:
            return False

    flashes = set()
    while any(energy_levels[i][j] != 0 for i in range(h) for j in range(w)):
        for i in range(h):
            for j in range(w):
                energy_levels[i][j] += 1
                if energy_levels[i][j] >= 10:
                    flashes.add((i, j))

        while flashes:
            i, j = flashes.pop()
            energy_levels[i][j] = 0
            for _i, _j in [
                (i - 1, j),
                (i - 1, j + 1),
                (i, j + 1),
                (i + 1, j + 1),
                (i + 1, j),
                (i + 1, j - 1),
                (i, j - 1),
                (i - 1, j - 1),
            ]:
                if _add_energy(_i, _j) is True:
                    flashes.add((_i, _j))
        step += 1

    return step


solution_function_01 = find_number_of_flashes_after_100_steps
solution_function_02 = find_all_octopuses_flash_step
