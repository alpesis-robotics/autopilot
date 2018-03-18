import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [12, 12]


def plot_grid(grid, path, start, goal):
    plt.imshow(grid, cmap="Greys", origin="lower")
    plt.xlabel('EAST')
    plt.ylabel('NORTH')

    plt.plot(start[1], start[0], 'x')
    plt.plot(goal[1], goal[0], 'x')
    plt.plot(np.array(path)[:, 1], np.array(path)[:, 0], 'g')
    plt.scatter(np.array(path)[:, 1], np.array(path)[:, 0])

    plt.xlabel('EAST')
    plt.ylabel('NORTH')

    plt.show()
