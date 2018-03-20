import numpy as np
from evals.heuristic import heuristic


def find_start_goal(edges, start, goal):
    distance_start_min = heuristic("euclidean", edges[0], start)
    distance_goal_min = heuristic("euclidean", edges[0], goal)
    near_start = (edges[0][0], edges[0][1])
    near_goal = (edges[0][0], edges[0][1])
    for x in edges[1:]:
        this_distance_start = heuristic("euclidean", x, start)
        this_distance_goal = heuristic("euclidean", x, goal)
        if this_distance_start < distance_start_min:
            distance_start_min = this_distance_start
            near_start = (x[0], x[1])
        if this_distance_goal < distance_goal_min:
            distance_goal_min = this_distance_goal
            near_goal = (x[0], x[1])
    return near_start, near_goal
