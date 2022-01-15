# Day 15: Chiton


def parse_file(fd):
    board = [list(map(int, line)) for line in fd.read().splitlines()]
    return (board,)


def lowest_total_risk_path(board):
    def _update_lowest_risks_cell(_h, _w):
        if cell_lowest_risks[_h][_w] is not None:
            cell_risks = cell_lowest_risks[_h][_w] + cell_risk
            if cell_risks < lowest_risks_cell[1]:
                return ((i, j), cell_risks)
        return lowest_risks_cell

    def _add_to_cell_stack(_h, _w):
        if cell_lowest_risks[_h][_w] is None and (_h, _w) not in cells_stack:
            cells_stack.add((_h, _w))

    inifinty_risk = 99999
    width = len(board[0])
    height = len(board)
    cell_lowest_risks = [[None for _ in range(width)] for _ in range(height)]
    cell_lowest_risks[0][0] = 0
    cells_stack = {(0, 1), (1, 0)}
    while cell_lowest_risks[-1][-1] is None:
        lowest_risks_cell = (None, inifinty_risk)
        for i, j in cells_stack:
            cell_risk = board[i][j]
            if i > 0:
                lowest_risks_cell = _update_lowest_risks_cell(i - 1, j)
            if j < width - 1:
                lowest_risks_cell = _update_lowest_risks_cell(i, j + 1)
            if i < height - 1:
                lowest_risks_cell = _update_lowest_risks_cell(i + 1, j)
            if j > 0:
                lowest_risks_cell = _update_lowest_risks_cell(i, j - 1)

        cells_stack.remove(lowest_risks_cell[0])
        c_h, c_w = lowest_risks_cell[0]
        cell_lowest_risks[c_h][c_w] = lowest_risks_cell[1]
        if c_h > 0:
            _add_to_cell_stack(c_h - 1, c_w)
        if c_w < width - 1:
            _add_to_cell_stack(c_h, c_w + 1)
        if c_h < height - 1:
            _add_to_cell_stack(c_h + 1, c_w)
        if c_w > 0:
            _add_to_cell_stack(c_h, c_w - 1)
    return cell_lowest_risks[-1][-1]


def lowest_total_risk_path_full_board(board):
    def _create_full_board(board):
        width = len(board[0])
        height = len(board)
        full_board = [[None for _ in range(5 * width)] for _ in range(5 * height)]
        for i in range(height):
            for j in range(width):
                value = board[i][j]
                for k in range(5):
                    for l in range(5):
                        updated_value = value + k + l
                        full_board[i + height * k][j + width * l] = (
                            updated_value if updated_value < 10 else updated_value - 9
                        )
        return full_board

    return lowest_total_risk_path(_create_full_board(board))


solution_function_01 = lowest_total_risk_path
solution_function_02 = lowest_total_risk_path_full_board
