# Day 20: Trench Map


def parse_file(fd):
    enhancement = [True if c == "#" else False for c in fd.readline().rstrip()]
    assert len(enhancement) == 512
    # empty line
    fd.readline()
    image = [
        ["1" if c == "#" else "0" for c in line] for line in fd.read().splitlines()
    ]
    return enhancement, image


def _transform_image(enhancement, image):
    infinity_margin = 4
    infinity_reducer = 2 * infinity_margin - 2

    for _ in range(2):
        image_width = len(image[0])
        image_height = len(image)

        inf_image_width = image_width + 2 * infinity_margin
        inf_image_height = image_height + 2 * infinity_margin
        inf_image = []
        for _ in range(infinity_margin):
            inf_image.append(["0"] * inf_image_width)
        for image_row in image:
            inf_image.append(
                ["0"] * infinity_margin + image_row + ["0"] * infinity_margin
            )
        for _ in range(infinity_margin):
            inf_image.append(["0"] * inf_image_width)

        post_image = [["0"] * inf_image_width for _ in range(inf_image_height)]
        for j in range(1, inf_image_height - 1):
            for i in range(1, inf_image_width - 1):
                pixel_value = "".join(
                    inf_image[j - 1][i - 1 : i + 2]
                    + inf_image[j][i - 1 : i + 2]
                    + inf_image[j + 1][i - 1 : i + 2]
                )
                if enhancement[int(pixel_value, 2)] is True:
                    post_image[j][i] = "1"

        image = post_image

    image = image[infinity_reducer:-infinity_reducer]
    for i in range(len(image)):
        image[i] = image[i][infinity_reducer:-infinity_reducer]

    return image


def transform_image(enhancement, image):
    image = _transform_image(enhancement, image)
    lit_pixels_counter = sum([image_row.count("1") for image_row in image])
    return lit_pixels_counter


def transform_image_50_times(enhancement, image):
    for _ in range(25):
        image = _transform_image(enhancement, image)
    lit_pixels_counter = sum([image_row.count("1") for image_row in image])
    return lit_pixels_counter


solution_function_01 = transform_image
solution_function_02 = transform_image_50_times
