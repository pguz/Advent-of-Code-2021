# Day 4: Giant Squid


def parse_file(fd):
    user_input = fd.readline().rstrip().split(",")
    fd.readline()  # empty line
    lines = fd.read().splitlines()

    boards = []
    boards_bingo_cands = dict()
    for i in range(len(lines) // 6):
        board_rows = []
        bingo_cands = []
        for j in range(5):
            row = lines[i * 6 + j].split()
            board_rows.append(row)
            bingo_cands.append(set(row))
        boards.append(board_rows)
        bingo_cands.extend([set([row[j] for row in board_rows]) for j in range(5)])
        boards_bingo_cands[i] = bingo_cands

    return user_input, boards, boards_bingo_cands


def calculate_bingo(user_input, bingo_boards, board_bingo_cands):
    last_input_number = None
    board_winner = None

    for input_number in user_input:
        for board_id, bingo_cands in board_bingo_cands.items():
            for cand in bingo_cands:
                cand.discard(input_number)
                if len(cand) == 0:
                    board_winner = board_id
                    last_input_number = input_number
                    break
            if board_winner is not None:
                break
        if board_winner is not None:
            break

    sum_unmarked_numbers_in_winner_board = sum(
        [sum(map(int, board_bingo_cands[board_winner][i])) for i in range(5)]
    )
    return sum_unmarked_numbers_in_winner_board * int(last_input_number)


def find_bingo_last_board(user_input, bingo_boards, board_bingo_cands):
    last_board_winner_cands = None
    last_user_input = None

    for input_number in user_input:
        for board_id, bingo_cands in board_bingo_cands.copy().items():
            for cands in bingo_cands:
                cands.discard(input_number)
                if len(cands) == 0:
                    last_board_winner_cands = board_bingo_cands.pop(board_id)
                    break
        if not board_bingo_cands:
            last_user_input = input_number
            break

    sum_unmarked_numbers_in_winner_board = sum(
        [sum(map(int, last_board_winner_cands[i])) for i in range(5)]
    )
    return sum_unmarked_numbers_in_winner_board * int(last_user_input)


solution_function_01 = calculate_bingo
solution_function_02 = find_bingo_last_board
