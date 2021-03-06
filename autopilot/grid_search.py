from grid.planning import a_star
from grid.prune import prune_path
from evals.heuristic import heuristic
from maps.visualize import plot_grid


def grid_search(grid, start, goal):
    path, cost = a_star(grid, heuristic, start, goal)
    print(len(path), cost)
    plot_grid(grid, path, start, goal)

    pruned_path = prune_path(path)
    print(len(pruned_path))
    # print(pruned_path)
    plot_grid(grid, pruned_path, start, goal)

