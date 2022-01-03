# Day 25: Sea Cucumber


def parse_file(fd):
    return (list(map(list, fd.read().splitlines())),)


def make_cucumbers_stop_moving(board):
    w = len(board[0])
    h = len(board)
    step = 0
    moves = w * h
    while moves != 0:
        moves = 0
        first_column = [line[0] for line in board]
        for i in range(w - 1):
            for j in range(h):
                if board[j][i] == ">" and board[j][i + 1] == ".":
                    board[j][i] = "."
                    board[j][i + 1] = "<"
                    moves += 1
                elif board[j][i] == "<":
                    board[j][i] = ">"
        for j in range(h):
            if board[j][w - 1] == ">" and first_column[j] == ".":
                board[j][w - 1] = "."
                board[j][0] = ">"
                moves += 1
            elif board[j][w - 1] == "<":
                board[j][w - 1] = ">"

        first_row = board[0].copy()
        for i in range(h - 1):
            for j in range(w):
                if board[i][j] == "v" and board[i + 1][j] == ".":
                    board[i][j] = "."
                    board[i + 1][j] = "^"
                    moves += 1
                elif board[i][j] == "^":
                    board[i][j] = "v"
        for i in range(w):
            if board[h - 1][i] == "v" and first_row[i] == ".":
                board[h - 1][i] = "."
                board[0][i] = "v"
                moves += 1
            elif board[h - 1][i] == "^":
                board[h - 1][i] = "v"
        step += 1
    return step


def collect_all_starts(*args, **kwargs):
    print("Not all stars have been collected yet.")
    return False


solution_function_01 = make_cucumbers_stop_moving
solution_function_02 = collect_all_starts
