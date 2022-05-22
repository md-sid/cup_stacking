import numpy as np


def algorithm_processing(data, number_of_cups):
    straight_cup = cup()
    flipped_cup = np.flipud(straight_cup)
    rows_in_cup = straight_cup.shape[0]
    cols_in_cup = straight_cup.shape[1]
    arr = np.zeros((number_of_cups * rows_in_cup, number_of_cups * cols_in_cup))
    num_rows = arr.shape[0]
    lines = data.readlines()

    for line in lines:
        line = line.replace(", ", "")
        line = line.strip()
        level, val, flip = line_processing(line, cols_in_cup)
        starting_row = num_rows - rows_in_cup * level
        ending_row = starting_row + rows_in_cup
        if flip:
            arr[starting_row:ending_row, val:val + cols_in_cup] = flipped_cup
        else:
            arr[starting_row:ending_row, val:val + cols_in_cup] = straight_cup

    return arr


def line_processing(line, cols_in_cup):
    val = 0
    flip = 0
    level = int(line[0])

    if line[1] != 'u':
        raise SystemExit('Pick up error in level ' + line[0])

    for i in line[2:-1]:
        if i == 'r':
            val += int(cols_in_cup / 2)
        elif i == 'l':
            val -= int(cols_in_cup / 2)
        elif i == 'f':
            flip = int(not flip)

    if line[-1] != 'd':
        raise SystemExit('Put down error in level ' + line[0])

    return level, val, flip


def cup():
    cup_array = np.array([[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 0, 0, 0, 0],
                          [0, 0, 0, 1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 1, 0, 0, 0],
                          [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                          [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                          [0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 0],
                          [0, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0],
                          [0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

    return cup_array
