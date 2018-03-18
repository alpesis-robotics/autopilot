import numpy as np

import settings
from data.grid import create_grid
from grid_search import grid_search


if __name__ == '__main__':
    data = np.loadtxt(settings.COLLIDERS, delimiter=",", dtype="Float64", skiprows=2)
    print(data)

    drone_altitude = 5
    safe_distance = 3
    grid = create_grid(data, drone_altitude, safe_distance)
   
    start = (25, 100)
    goal = (750., 370.)
    grid_search(grid, start, goal)
