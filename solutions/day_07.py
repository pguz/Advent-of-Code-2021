# Day 7: The Treachery of Whales


def parse_file(fd):
    return (list(map(int, fd.readline().split(","))),)


def calculate_fuel_spent_to_aligned_position(positions):
    positions = sorted(positions)
    aligned_position = positions[len(positions) // 2]
    fuel_spent = sum([abs(aligned_position - p) for p in positions])
    return fuel_spent


def calculate_fuel_spent_to_aligned_position_with_progression(positions):
    fuel_spent = min(
        [
            sum(
                [
                    abs(aligned_position - p) * (abs(aligned_position - p) + 1) / 2
                    for p in positions
                ]
            )
            for aligned_position in positions
        ]
    )
    return fuel_spent


solution_function_01 = calculate_fuel_spent_to_aligned_position
solution_function_02 = calculate_fuel_spent_to_aligned_position_with_progression
