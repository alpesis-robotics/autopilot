import numpy as np

from medialaxis.planning import a_star
from medialaxis.prune import heuristic
from medialaxis.prune import prune_path
from medialaxis.prune import find_start_goal
from maps.visualize import plot_medial_map


def medial_search(grid, skeleton, start, goal):
    skel_start, skel_goal = find_start_goal(skeleton, start, goal)
    print(start, goal)
    print(skel_start, skel_goal)

    path, cost = a_star(skeleton, heuristic, skel_start, skel_goal)
    print(len(path), cost)
    plot_medial_map(grid, skeleton, path, start, goal, skel_start, skel_goal)

    #pruned_path = prune_path(path)
    #print(len(pruned_path))
    #print(pruned_path)
    #plot_medial_map(grid, pruned_path, start, goal)
