# Day 8: Seven Segment Search


def parse_file(fd):
    list_of_digits_with_output = []
    for line in fd.read().splitlines():
        digits, output = line.split("|")
        list_of_digits_with_output.append((digits.split(), output.split()))
    return (list_of_digits_with_output,)


def count_1_4_7_8_displayed_digits(list_of_digits_with_output):
    return sum(
        [
            len([output for output in outputs if len(output) in [2, 3, 4, 7]])
            for _, outputs in list_of_digits_with_output
        ]
    )


def sum_output_displayed_numbers(list_of_digits_with_output):
    result = 0
    for digits, outputs in list_of_digits_with_output:
        digits_by_length = sorted(digits, key=len)
        digit_symbols = {}
        digit_symbols[1] = set(digits_by_length[0])
        digit_symbols[7] = set(digits_by_length[1])
        digit_symbols[4] = set(digits_by_length[2])
        digit_symbols[8] = set(digits_by_length[9])
        for i in range(3):
            symbols = set(digits_by_length[6 + i])
            if not digit_symbols[1].issubset(symbols):
                digit_symbols[6] = symbols
                continue
            elif not digit_symbols[4].issubset(symbols):
                digit_symbols[0] = symbols
                continue
            digit_symbols[9] = symbols
        for i in range(3):
            symbols = set(digits_by_length[3 + i])
            if digit_symbols[1].issubset(symbols):
                digit_symbols[3] = symbols
                continue
            elif symbols.issubset(digit_symbols[6]):
                digit_symbols[5] = symbols
                continue
            digit_symbols[2] = symbols

        displayed_number = 0
        for output_symbols in outputs:
            for digit, symbols in digit_symbols.items():
                if set(output_symbols) == symbols:
                    displayed_number = 10 * displayed_number + digit
                    break
        result += displayed_number
    return result


solution_function_01 = count_1_4_7_8_displayed_digits
solution_function_02 = sum_output_displayed_numbers
