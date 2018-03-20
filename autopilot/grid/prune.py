import numpy as np


def point(p):
    return np.array([p[0], p[1], 1.]).reshape(1, -1)


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
