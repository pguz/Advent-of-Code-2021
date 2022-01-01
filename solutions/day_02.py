# Day 2: Dive!


def parse_file(fd):
    return [fd.read().splitlines()]


def simple_control(commands):
    x, y = 0, 0
    for command in commands:
        d, v = command.split()
        v = int(v)
        # if statement occurred to be much faster than functional equivalents
        if d == "forward":
            x += v
        elif d == "up":
            y -= v
        elif d == "down":
            y += v
    return abs(x * y)


def complex_control(commands):
    a, x, y = 0, 0, 0
    for command in commands:
        d, v = command.split()
        v = int(v)
        # if statement occurred to be much faster than functional equivalents
        if d == "forward":
            x += v
            y += a * v
        elif d == "up":
            a -= v
        elif d == "down":
            a += v
    return abs(x * y)


solution_function_01 = simple_control
solution_function_02 = complex_control
