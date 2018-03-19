import numpy as np

def distance(x, y):
    return np.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


def find_start_goal(skel, start, goal):
    skel_true = np.nonzero(skel)
    skel_trans = np.transpose(skel_true)
    distance_start_min = distance(skel_trans[0], start)
    distance_goal_min = distance(skel_trans[0], goal)
    near_start = (skel_trans[0][0], skel_trans[0][1])
    near_goal = (skel_trans[0][0], skel_trans[0][1])
    for x in skel_trans[1:]:
        this_distance_start = distance(x, start)
        this_distance_goal = distance(x, goal)
        if this_distance_start < distance_start_min:
            distance_start_min = this_distance_start
            near_start = (x[0], x[1])
        if this_distance_goal < distance_goal_min:
            distance_goal_min = this_distance_goal
            near_goal = (x[0], x[1])
    return near_start, near_goal


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
