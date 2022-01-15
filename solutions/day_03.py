# Day 3: Binary Diagnostic


def parse_file(fd):
    return (fd.read().splitlines(),)


def calculate_power_consumption(measurements):
    threshold = len(measurements) / 2

    onces = map(lambda l: l.count("1") > threshold, zip(*map(list, measurements)))

    gamma_rate = "".join(map(str, map(int, onces)))
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
    co2_scrubber_rating = _calculate_rating(lambda v: "0" if v >= 0 else "1")

    return oxygen_generator_rating * co2_scrubber_rating


solution_function_01 = calculate_power_consumption
solution_function_02 = calculate_life_support_rating
