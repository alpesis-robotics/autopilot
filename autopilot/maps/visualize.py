import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [12, 12]


def plot_grid(grid, path, start, goal):
    plt.imshow(grid, cmap="Greys", origin="lower")

    plt.plot(start[1], start[0], 'x')
    plt.plot(goal[1], goal[0], 'x')
    plt.plot(np.array(path)[:, 1], np.array(path)[:, 0], 'g')
    plt.scatter(np.array(path)[:, 1], np.array(path)[:, 0])

    plt.xlabel('EAST')
    plt.ylabel('NORTH')

    plt.show()


def plot_graph(grid, edges, path, start, goal, near_start, near_goal):
    plt.imshow(grid, cmap="Greys", origin="lower")

    for e in edges:
        p1 = e[0]
        p2 = e[1]
        plt.plot([p1[1], p2[1]], [p1[0], p2[0]], 'b-')

    plt.plot(start[1], start[0], 'x')
    plt.plot(goal[1], goal[0], 'x')
    plt.plot(near_start[1], near_start[0], 'rx')
    plt.plot(near_goal[1], near_goal[0], 'rx')
    plt.plot(np.array(path)[:, 1], np.array(path)[:, 0], 'g')
    plt.scatter(np.array(path)[:, 1], np.array(path)[:, 0])

    plt.xlabel('EAST')
    plt.ylabel('NORTH')

    plt.show()


def plot_medial_map(grid, skeleton, path, start, goal, skel_start, skel_goal):
    plt.imshow(grid, cmap="Greys", origin="lower")
    plt.imshow(skeleton, cmap="Greys", origin="lower", alpha=0.7)

    plt.plot(start[1], start[0], 'rx')
    plt.plot(goal[1], goal[0], 'rx')
    plt.plot(skel_start[1], skel_start[0], 'x')
    plt.plot(skel_goal[1], skel_goal[0], 'x')

    plt.plot(np.array(path)[:, 1], np.array(path)[:, 0], 'g')
    plt.scatter(np.array(path)[:, 1], np.array(path)[:, 0])

    plt.xlabel('EAST')
    plt.ylabel('NORTH')

    plt.show()

