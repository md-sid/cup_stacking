import numpy as np
from utils import algorithm_processing
import matplotlib.pyplot as plt


def main(alg):
    # number_of_cups = input('Enter the total number of cups: ')
    number_of_cups = 10

    result = algorithm_processing(alg, number_of_cups)

    result = result[~np.all(result == 0, axis=1)]  # removes rows of zeros
    result = result[:, ~np.all(result == 0, axis=0)]  # removes columns of zeros

    return result


if __name__ == '__main__':
    data = open('sample_input1.txt', 'r')
    output = main(data)
    plt.matshow(output, cmap=plt.cm.jet)
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    plt.show()
    plt.imsave(data.name[0:-4] + '.png', output, cmap=plt.cm.jet)
