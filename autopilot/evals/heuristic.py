import numpy as np


def heuristic(ftype, x1, x2):
    if ftype == "euclidean":
        return np.sqrt((x1[0] - x2[0])**2 + (x1[1] - x2[1])**2)

    elif ftype == "manhanttan":
        return np.abs(x1[0] - x2[0]) + np.abs(x1[1] - x2[1])
