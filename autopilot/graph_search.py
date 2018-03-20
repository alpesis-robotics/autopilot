from graph.planning import a_star


def graph_search(grid, edges, start, goal):
    path, cost = a_star(grid, heuristic, start, goal)
    #print(len(path), cost)
    #plot_grid(grid, path, start, goal)

    #pruned_path = prune_path(path)
    #print(len(pruned_path))
    # print(pruned_path)
    #plot_grid(grid, pruned_path, start, goal)
