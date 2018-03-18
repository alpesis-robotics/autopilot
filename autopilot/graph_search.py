from maps.visualize import plot_medial_map
from graph.prune import find_start_goal


def graph_search(grid, skeleton, start, goal):
    plot_medial_map(grid, skeleton, start, goal)
    skel_start, skel_goal = find_start_goal(skeleton, start, goal)
    print(start, goal)
    print(skel_start, skel_goal)
