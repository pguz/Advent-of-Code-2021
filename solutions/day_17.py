# Day 17: Trick Shot


def parse_file(fd):
    x_coords, y_coords = fd.readline().strip().split(": ")[1].split(", ")
    x_coords = tuple(map(int, x_coords.split("=")[1].split("..")))
    y_coords = tuple(map(int, y_coords.split("=")[1].split("..")))
    return ((x_coords, y_coords),)


def find_highest_y_position(target_coords):
    y_fall = abs(target_coords[1][0])
    return y_fall * (y_fall - 1) // 2


def count_target_velocities(target_coords):
    x_coords, y_coords = target_coords
    vx_min = int((-1 + pow(1 + 8 * x_coords[0], 0.5)) / 2)
    vx_max = x_coords[1]
    vy_min = -abs(y_coords[0])
    vy_max = abs(y_coords[0])

    target_velocities = 0
    for i in range(vx_min, vx_max + 1):
        for j in range(vy_min, vy_max + 1):
            vx, vy = i, j
            x, y = 0, 0
            while x <= x_coords[1] and y >= y_coords[0]:
                x += vx
                y += vy
                if (
                    x_coords[0] <= x
                    and x <= x_coords[1]
                    and y_coords[0] <= y
                    and y <= y_coords[1]
                ):
                    target_velocities += 1
                    break
                if vx > 0:
                    vx -= 1
                vy -= 1

    return target_velocities


solution_function_01 = find_highest_y_position
solution_function_02 = count_target_velocities
