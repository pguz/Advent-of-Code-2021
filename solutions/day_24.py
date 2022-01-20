# Day 24: Arithmetic Logic Unit


def parse_file(fd):
    return ([line.split() for line in fd.read().splitlines()],)


def _find_monad_depends(instructions):
    def chunk_by_input_command(instructions):
        for i in range(0, len(instructions), 18):
            yield instructions[i : i + 18]

    stack = list()
    depends = list()
    for input_id, commands in enumerate(chunk_by_input_command(instructions)):
        dependency_addition = int(commands[5][2])
        input_addition = int(commands[15][2])
        z_divider = commands[4][2]
        if not stack:
            depend_id, depend_value = None, 0
        elif z_divider == "26":
            depend_id, depend_value = stack.pop()
        else:
            depend_id, depend_value = stack[-1]
        depend_value += dependency_addition
        if (-9 <= depend_value) and (depend_value <= 9):
            depends.append((input_id, depend_id, depend_value))
        else:
            stack.append((input_id, input_addition))

    assert not stack

    return depends


def find_largest_monad_number(instructions):
    depends = _find_monad_depends(instructions)
    assert len(depends) == 7
    result = [None for _ in range(14)]

    for index_1, index_2, diff in depends:
        if diff > 0:
            result[index_1] = "9"
            result[index_2] = str(9 - diff)
        else:
            result[index_1] = str(9 + diff)
            result[index_2] = "9"

    return int("".join(result))


def find_smallest_monad_number(instructions):
    depends = _find_monad_depends(instructions)
    assert len(depends) == 7
    result = [None for _ in range(14)]

    for index_1, index_2, diff in depends:
        if diff < 0:
            result[index_1] = "1"
            result[index_2] = str(1 - diff)
        else:
            result[index_1] = str(1 + diff)
            result[index_2] = "1"

    return int("".join(result))


solution_function_01 = find_largest_monad_number
solution_function_02 = find_smallest_monad_number
