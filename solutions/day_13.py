# Day 13: Transparent Origami


def parse_file(fd):
    dots = list()
    line = fd.readline().rstrip()
    while line:
        x, y = line.split(',')
        dots.append((int(x), int(y)))
        line = fd.readline().rstrip()

    folds = list()
    line = fd.readline().rstrip()
    while line:
        direction, value = line.split('=')
        folds.append((direction.split()[2], int(value)))
        line = fd.readline().rstrip()

    return [dots, folds]


def find_dots_number_after_first_fold(dots, folds):
    first_fold = folds[0]
    dots_after_folding = set()

    folded_paper_dimension = first_fold[1]
    if first_fold[0] == 'y':
        dots = zip(*dots)
        dots = zip(dots[1], dots[0])

    for x, y in dots:
        dots_after_folding.add((folded_paper_dimension - abs(folded_paper_dimension - x), y))

    return len(dots_after_folding)


def execute_folds(dots, folds):
    post_dots = set(dots)
    for fold in folds:
        pre_dots = post_dots
        post_dots = set()
        for x, y in pre_dots:
            if fold[0] == 'x' and x >= fold[1]:
                post_dots.add((2 * fold[1] - x, y))
            elif fold[0] == 'y' and y >= fold[1]:
                post_dots.add((x, 2 * fold[1] - y))
            else:
                post_dots.add((x, y))

    debug = False
    if debug is True:
        xs, ys = zip(*post_dots)
        paper_width = max(xs) + 1
        paper_height = max(ys) + 1
        paper = [['.' for _ in range(paper_width)] for _ in range(paper_height)]
        for x, y in post_dots:
            paper[y][x] = '#'

        for i in range(paper_height):
            print(''.join(paper[i]))

    return len(post_dots)


solution_function_01 = find_dots_number_after_first_fold
solution_function_02 = execute_folds
