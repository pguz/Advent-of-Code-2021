# Day 19: Beacon Scanner


def parse_file(fd):
    scanners = []
    for line in fd.read().splitlines():
        if "scanner" in line:
            scanners.append([])
            continue
        if not line:
            continue
        scanners[-1].append(list(map(int, line.rstrip().split(","))))
    return (scanners,)


def _distances_between_beacons(beacons):
    distances = dict()
    for i in range(len(beacons)):
        for j in range(i):
            distance = sum([pow(beacons[i][k] - beacons[j][k], 2) for k in range(3)])
            distances[distance] = (i, j)
    return distances


def _find_common_beacons(
    beacons_1, distances_between_beacons_1, beacons_2, distances_between_beacons_2
):
    def _get_unique_values_from_set_of_pairs(set_of_pairs):
        unique_values = set()
        for v1, v2 in set_of_pairs:
            unique_values.add(v1)
            unique_values.add(v2)
        return unique_values

    the_same_distances_between_beacons = set(
        distances_between_beacons_1.keys()
    ).intersection(set(distances_between_beacons_2.keys()))
    common_beacons_indexes_1 = _get_unique_values_from_set_of_pairs(
        distances_between_beacons_1[d] for d in the_same_distances_between_beacons
    )
    common_beacons_indexes_2 = _get_unique_values_from_set_of_pairs(
        distances_between_beacons_2[d] for d in the_same_distances_between_beacons
    )
    common_beacons_1 = [beacons_1[i] for i in common_beacons_indexes_1]
    common_beacons_2 = [beacons_2[i] for i in common_beacons_indexes_2]

    return common_beacons_1, common_beacons_2


def _find_transform_funcs(coords_1, coords_2):
    def _find_transform_func(bd, dbd, ddx, ddy, ddz):
        if dbd == ddx:
            return 0, lambda v: v - (x_2[0] - bd[0])
        if dbd == ddy:
            return 1, lambda v: v - (y_2[0] - bd[0])
        if dbd == ddz:
            return 2, lambda v: v - (z_2[0] - bd[0])
        if dbd == ddx[::-1]:
            return 3, lambda v: -v + (x_2[0] + bd[-1])
        if dbd == ddy[::-1]:
            return 4, lambda v: -v + (y_2[0] + bd[-1])
        if dbd == ddz[::-1]:
            return 5, lambda v: -v + (z_2[0] + bd[-1])
        raise ValueError("Common dimension has not been found.")

    x_1, y_1, z_1 = list(sorted(d) for d in zip(*coords_1))
    x_2, y_2, z_2 = list(sorted(d) for d in zip(*coords_2))

    dx_1 = [n - p for n, p in zip(x_1[1:], x_1[:-1])]
    dy_1 = [n - p for n, p in zip(y_1[1:], y_1[:-1])]
    dz_1 = [n - p for n, p in zip(z_1[1:], z_1[:-1])]
    dx_2 = [n - p for n, p in zip(x_2[1:], x_2[:-1])]
    dy_2 = [n - p for n, p in zip(y_2[1:], y_2[:-1])]
    dz_2 = [n - p for n, p in zip(z_2[1:], z_2[:-1])]

    return [
        _find_transform_func(bd, dd, dx_2, dy_2, dz_2)
        for bd, dd in [(x_1, dx_1), (y_1, dy_1), (z_1, dz_1)]
    ]


def _find_all_transforms_funcs(scanners):
    beacons_distances_by_scanner = [_distances_between_beacons(s) for s in scanners]

    base_indexes = {0}
    to_process_indexes = {*range(len(scanners))}
    transform_funcs_dict = {0: []}
    while base_indexes:
        base_index = base_indexes.pop()
        to_process_indexes.remove(base_index)
        for current_index in to_process_indexes:
            common_beacons_1, common_beacons_2 = _find_common_beacons(
                scanners[base_index],
                beacons_distances_by_scanner[base_index],
                scanners[current_index],
                beacons_distances_by_scanner[current_index],
            )

            if len(common_beacons_1) < 12:
                continue

            base_indexes.add(current_index)

            bx, by, bz = list(sorted(d) for d in zip(*common_beacons_1))
            dx, dy, dz = list(sorted(d) for d in zip(*common_beacons_2))

            transform_funcs = _find_transform_funcs(common_beacons_1, common_beacons_2)
            transform_funcs_dict[current_index] = [
                *(transform_funcs_dict[base_index]),
                transform_funcs,
            ]

    return transform_funcs_dict


def find_all_beacons(scanners):
    transform_funcs_dict = _find_all_transforms_funcs(scanners)

    unique_beacons = set()
    unique_beacons |= {tuple(b) for b in scanners[0]}
    for j in range(1, len(scanners)):
        dims = list(zip(*scanners[j]))
        for k in range(len(transform_funcs_dict[j]))[::-1]:
            transform_funcs = transform_funcs_dict[j][k]
            xs = [transform_funcs[0][1](v) for v in dims[transform_funcs[0][0] % 3]]
            ys = [transform_funcs[1][1](v) for v in dims[transform_funcs[1][0] % 3]]
            zs = [transform_funcs[2][1](v) for v in dims[transform_funcs[2][0] % 3]]
            dims = (xs, ys, zs)

        unique_beacons |= {tuple(b) for b in zip(xs, ys, zs)}

    return len(unique_beacons)


def find_max_distance_between_scanners(scanners):
    transform_funcs_dict = _find_all_transforms_funcs(scanners)

    scaners_coords = [(0, 0, 0)]

    for j in range(1, len(scanners)):
        scanner_coords = (0, 0, 0)
        for k in range(len(transform_funcs_dict[j]))[::-1]:
            transform_funcs = transform_funcs_dict[j][k]
            x = transform_funcs[0][1](scanner_coords[transform_funcs[0][0] % 3])
            y = transform_funcs[1][1](scanner_coords[transform_funcs[1][0] % 3])
            z = transform_funcs[2][1](scanner_coords[transform_funcs[2][0] % 3])
            scanner_coords = (x, y, z)
        scaners_coords.append(scanner_coords)

    max_distance = 0
    for i in range(len(scaners_coords)):
        for j in range(i):
            distance = sum(
                [abs(scaners_coords[i][k] - scaners_coords[j][k]) for k in range(3)]
            )
            if distance > max_distance:
                max_distance = distance

    return max_distance


solution_function_01 = find_all_beacons
solution_function_02 = find_max_distance_between_scanners
