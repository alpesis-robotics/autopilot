import numpy as np
import networkx as nx

from graph.planning import a_star
from graph.prune import find_start_goal
from evals.heuristic import heuristic
from maps.visualize import plot_graph


def graph_search(grid, edges, start, goal):
    G = nx.Graph()
    for e in edges:
        p1 = e[0]
        p2 = e[1]
        dist = np.linalg.norm(np.array(p2) - np.array(p1))
        G.add_edge(p1, p2, weight=dist)

    path, cost = a_star(G.edges(), heuristic, start, goal)
    print(len(path), cost)
    #plot_graph(grid, edges, path, start, goal, near_start, near_goal)

    #pruned_path = prune_path(path)
    #print(len(pruned_path))
    # print(pruned_path)
    #plot_grid(grid, pruned_path, start, goal)
