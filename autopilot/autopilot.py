import numpy as np
from skimage.util import invert
from skimage.morphology import medial_axis

import settings
from maps.grid import create_grid
from grid_search import grid_search
from medial_search import medial_search
from graph_search import graph_search


if __name__ == '__main__':
    data = np.loadtxt(settings.COLLIDERS, delimiter=",", dtype="Float64", skiprows=2)
    print(data)

    drone_altitude = 5
    safe_distance = 3
    grid = create_grid(data, drone_altitude, safe_distance)
    skeleton = medial_axis(invert(grid))
   
    start = (25, 100)
    goal = (750., 370.)
    grid_search(grid, start, goal)

    start = (25, 100)
    goal = (750., 370.)
    medial_search(grid, skeleton, start, goal)

    start = (25, 100)
    goal = (650., 500)
    # graph_search(grid, skeleton, start, goal)
