# Day 3: Binary Diagnostic


def parse_file(fd):
    return [fd.read().splitlines()]


def calculate_power_consumption(measurements):
    # The fastest found bit_counter
    bits_counter = map(lambda l: "".join(l).count("1"), zip(*map(list, measurements)))

    threshold = len(measurements) / 2
    gamma_rate = "".join(["1" if value > threshold else "0" for value in bits_counter])
    gamma_rate = int(gamma_rate, 2)

    sample_size = len(measurements[0])
    epsilon_rate = pow(2, sample_size) - gamma_rate - 1

    return gamma_rate * epsilon_rate


def calculate_life_support_rating(measurements):
    def _calculate_rating(condition):
        candidates = set(measurements)
        i = 0
        while len(candidates) > 1:
            ones_candidates = {c for c in candidates if c[i] == "1"}
            zeros_candidates = candidates - ones_candidates
            bit_selected = condition(len(ones_candidates) - len(zeros_candidates))
            candidates = ones_candidates if bit_selected == "1" else zeros_candidates
            i += 1
        return int(candidates.pop(), 2)

    oxygen_generator_rating = _calculate_rating(lambda v: "1" if v >= 0 else "0")
    CO2_scrubber_rating = _calculate_rating(lambda v: "0" if v >= 0 else "1")

    return oxygen_generator_rating * CO2_scrubber_rating


solution_function_01 = calculate_power_consumption
solution_function_02 = calculate_life_support_rating
