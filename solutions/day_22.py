# Day 22: Reactor Reboot


def parse_file(fd):
    steps = []
    for line in fd.read().splitlines():
        switch, coords = line.split()
        x_part, y_part, z_part = coords.split(",")
        x_coords = tuple(map(int, x_part.split("=")[1].split("..")))
        y_coords = tuple(map(int, y_part.split("=")[1].split("..")))
        z_coords = tuple(map(int, z_part.split("=")[1].split("..")))
        steps.append((True if switch == "on" else False, x_coords, y_coords, z_coords))
    return (steps,)


def count_turned_on_cubes_small_space(steps):
    space_limits = 50
    space_size = space_limits * 2 + 1
    cubes = [
        [[False for _ in range(space_size)] for _ in range(space_size)]
        for _ in range(space_size)
    ]

    for switch, xs, ys, zs in steps[:20]:
        for i in range(xs[0] + space_limits, xs[1] + space_limits + 1):
            for j in range(ys[0] + space_limits, ys[1] + space_limits + 1):
                for k in range(zs[0] + space_limits, zs[1] + space_limits + 1):
                    cubes[i][j][k] = switch

    return sum([sum([sum(cells) for cells in layers]) for layers in cubes])


def count_turned_on_cubes_large_space(steps):
    class Cuboid:
        def __init__(self, switch, xs, ys, zs):
            self.switch = switch
            self.xs = xs
            self.ys = ys
            self.zs = zs

        def volume(self):
            if self.switch is False:
                return 0
            return (
                (self.xs[1] - self.xs[0] + 1)
                * (self.ys[1] - self.ys[0] + 1)
                * (self.zs[1] - self.zs[0] + 1)
            )

    def _create_coords_line(fcs, ccs):
        if fcs[0] < ccs[0]:
            if fcs[1] < ccs[1]:
                return (
                    (fcs[0], ccs[0] - 1, 0),
                    (ccs[0], fcs[1], 1),
                    (fcs[1] + 1, ccs[1], 2),
                )
            else:
                return (
                    (fcs[0], ccs[0] - 1, 0),
                    (ccs[0], ccs[1], 1),
                    (ccs[1] + 1, fcs[1], 0),
                )
        else:
            if fcs[1] < ccs[1]:
                return (
                    (ccs[0], fcs[0] - 1, 2),
                    (fcs[0], fcs[1], 1),
                    (fcs[1] + 1, ccs[1], 2),
                )
            else:
                return (
                    (ccs[0], fcs[0] - 1, 2),
                    (fcs[0], ccs[1], 1),
                    (ccs[1] + 1, fcs[1], 0),
                )

    entry_cuboids = [Cuboid(*step) for step in steps]
    final_cuboids = []

    for entry_cuboid in entry_cuboids[::-1]:
        current_cuboids = [entry_cuboid]

        for fixed_cuboid in final_cuboids:
            splitted_cuboids = list()
            for cuboid in current_cuboids:
                if (
                    fixed_cuboid.xs[0] <= cuboid.xs[1]
                    and cuboid.xs[0] <= fixed_cuboid.xs[1]
                    and fixed_cuboid.ys[0] <= cuboid.ys[1]
                    and cuboid.ys[0] <= fixed_cuboid.ys[1]
                    and fixed_cuboid.zs[0] <= cuboid.zs[1]
                    and cuboid.zs[0] <= fixed_cuboid.zs[1]
                ):
                    xl = _create_coords_line(fixed_cuboid.xs, cuboid.xs)
                    yl = _create_coords_line(fixed_cuboid.ys, cuboid.ys)
                    zl = _create_coords_line(fixed_cuboid.zs, cuboid.zs)

                    for xp in xl:
                        for yp in yl:
                            for zp in zl:
                                if (xp[2] == 2 or yp[2] == 2 or zp[2] == 2) and not (
                                    xp[2] == 0 or yp[2] == 0 or zp[2] == 0
                                ):
                                    splitted_cuboids.append(
                                        Cuboid(cuboid.switch, xp, yp, zp)
                                    )
                else:
                    splitted_cuboids.append(cuboid)
            current_cuboids = splitted_cuboids
        final_cuboids.extend(current_cuboids)

    return sum([c.volume() for c in final_cuboids])


solution_function_01 = count_turned_on_cubes_small_space
solution_function_02 = count_turned_on_cubes_large_space
