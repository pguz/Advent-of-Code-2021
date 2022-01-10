# Day 21: Dirac Dice
from functools import lru_cache


def parse_file(fd):
    f_pos = int(fd.readline().split(":")[1])
    s_pos = int(fd.readline().split(":")[1])
    return ((f_pos, s_pos),)


def calculate_winner_deterministic_die(starting_positions):
    dices = [6, 5, 4, 3, 2, 1, 0, 9, 8, 7]
    f_pos, s_pos = starting_positions
    f_pkt, s_pkt = 0, 0
    turn = 0

    def _make_move(pos, turn):
        return (pos + dices[turn % 10] - 1) % 10 + 1

    while f_pkt < 1000 and s_pkt < 1000:
        f_pos = _make_move(f_pos, turn)
        f_pkt += f_pos
        turn += 1
        if f_pkt >= 1000:
            break
        s_pos = _make_move(s_pos, turn)
        s_pkt += s_pos
        turn += 1

    subturns = 3 * turn

    return subturns * (s_pkt if f_pkt >= 1000 else f_pkt)


def calculate_winner_quantum_die(starting_positions):
    def _make_move(pos, value):
        return (pos + value - 1) % 10 + 1

    @lru_cache(maxsize=None)
    def make_subturn(f_pos, f_pkt, s_pos, s_pkt, player, subturn, dice_value):
        subturn += 1
        if player is True:
            f_pos = _make_move(f_pos, dice_value)
        else:
            s_pos = _make_move(s_pos, dice_value)
        if subturn == 3:
            if player is True:
                f_pkt += f_pos
                if f_pkt >= 21:
                    return 1
                player = False
            else:
                s_pkt += s_pos
                if s_pkt >= 21:
                    return 0
                player = True
            subturn = 0
        return sum(
            [
                make_subturn(f_pos, f_pkt, s_pos, s_pkt, player, subturn, dice_side)
                for dice_side in range(1, 4)
            ]
        )

    f_pos, s_pos = starting_positions
    f_pkt, s_pkt = 0, 0

    return sum(
        [
            make_subturn(
                f_pos,
                f_pkt,
                s_pos,
                s_pkt,
                player=True,
                subturn=0,
                dice_value=dice_side,
            )
            for dice_side in range(1, 4)
        ]
    )


solution_function_01 = calculate_winner_deterministic_die
solution_function_02 = calculate_winner_quantum_die
