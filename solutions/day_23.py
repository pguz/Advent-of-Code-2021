# Day 23: Amphipod


def parse_file(fd):
    lines = fd.read().splitlines()
    return [
        (
            [lines[2][3], lines[3][3]],
            [lines[2][5], lines[3][5]],
            [lines[2][7], lines[3][7]],
            [lines[2][9], lines[3][9]],
        )
    ]


def organize_the_amphipods_simple(initial_configuration):
    print("This task has been resolved manually, without any code implementation")
    return True


def organize_the_amphipods_complex(initial_configuration):
    print("This task has been resolved manually, without any code implementation")
    return True


solution_function_01 = organize_the_amphipods_simple
solution_function_02 = organize_the_amphipods_complex
