import numpy as np
import matplotlib.pyplot as plt

from grid import create_grid
from planning import a_star

plt.rcParams["figure.figsize"] = [12, 12]


def point(p):
    return np.array([p[0], p[1], 1.]).reshape(1, -1)


def heuristic(position, goal_position):
    # return np.sqrt((position[0] - goal_position[0])**2 + (position[1] - goal_position[1])**2)
    return np.abs(position[0] - goal_position[0]) + np.abs(position[1] - goal_position[1])


def collinearity_check(p1, p2, p3, epsilon=1e-6):
    m = np.concatenate((p1, p2, p3), 0)
    det = np.linalg.det(m)
    return abs(det) < epsilon


def prune_path(path):
    #pruned_path = [path[0]]
    #for i in range(len(path)-2):
    #    if not collinearity_check(point(path[i]), point(path[i+1]), point(path[i+2])):
    #        pruned_path.append(path[i])
    #pruned_path.append(path[-1])
    pruned_path = [p for p in path]
    i = 0
    while i < (len(pruned_path) - 2):
        if collinearity_check(point(pruned_path[i]), point(pruned_path[i+1]), point(pruned_path[i+2])):
            pruned_path.remove(pruned_path[i+1])
        else:
            i += 1
    return pruned_path


def plot(grid, path, start, goal):
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



if __name__ == '__main__':
    filename = "colliders.csv"
    data = np.loadtxt(filename, delimiter=",", dtype="Float64", skiprows=2)
    print(data)

    drone_altitude = 5
    safe_distance = 3
    grid = create_grid(data, drone_altitude, safe_distance)

    start = (25, 100)
    goal = (750., 370.)
    path, cost = a_star(grid, heuristic, start, goal)
    print(len(path), cost)
    plot(grid, path, start, goal)

    pruned_path = prune_path(path)
    print(len(pruned_path))
    # print(pruned_path)
    plot(grid, pruned_path, start, goal)