# Day 10: Syntax Scoring


def parse_file(fd):
    return (list(fd.read().splitlines()),)


def calculate_total_syntax_error_score(chunks):
    paranthesis_pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    illegal_character_pentlies = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    error_score = 0
    openings = paranthesis_pairs.values()
    for chunk in chunks:
        stack = list()
        for c in chunk:
            if c in openings:
                stack.append(c)
            else:
                matching_element = stack.pop()
                if paranthesis_pairs[c] != matching_element:
                    error_score += illegal_character_pentlies[c]
    return error_score


def get_middle_score_of_autocompletion(chunks):
    autocompletion_points = []
    paranthesis_pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    illegal_character_pentlies = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }
    openings = paranthesis_pairs.values()
    for chunk in chunks:
        stack = list()
        valid_chunk = True
        for c in chunk:
            if c in openings:
                stack.append(c)
            else:
                matching_element = stack.pop()
                if paranthesis_pairs[c] != matching_element:
                    valid_chunk = False
                    break
        if valid_chunk is True:
            points = 0
            while stack:
                points = points * 5 + illegal_character_pentlies[stack.pop()]
            autocompletion_points.append(points)
    return sorted(autocompletion_points)[len(autocompletion_points) // 2]


solution_function_01 = calculate_total_syntax_error_score
solution_function_02 = get_middle_score_of_autocompletion
