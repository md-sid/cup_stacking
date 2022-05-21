import numpy as np


def algorithm_processing(data, number_of_cups):
    arr = np.zeros((number_of_cups * 14, number_of_cups * 18))
    num_rowws = arr.shape[0]
    lines = data.readlines()
    straight_cup = cup()
    flipped_cup = np.flipud(straight_cup)

    for line in lines:
        line = line.replace(", ", "")
        line = line.strip()
        level, val, flip = line_processing(line)
        starting_row = num_rowws - 14*level
        ending_row = starting_row + 14
        if flip:
            arr[starting_row:ending_row, val:val+18] = flipped_cup
        else:
            arr[starting_row:ending_row, val:val + 18] = straight_cup

    return arr


def line_processing(line):
    val = 0
    flip = 0
    level = int(line[0])

    if line[1] != 'u':
        raise SystemExit('Pick up error in level ' + line[0])

    for i in line[2:-1]:
        if i == 'r':
            val += 9
        elif i == 'l':
            val -= 9
        elif i == 'f':
            flip = int(not flip)

    if line[-1] != 'd':
        raise SystemExit('Put down error in level ' + line[0])

    return level, val, flip


def cup():
    cup_array = np.array([[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
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
