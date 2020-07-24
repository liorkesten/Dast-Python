def cc(g):
    """
    Function that counting the comp connectivity in the graph and return
    the num of them
                             Time Complexity : O(|V|+|E|)
    :param g: graph
    :return:
    """
    # Reset the dist and visited of each vertex
    for vertex in g.vertices:
        vertex.dist, vertex.visited = g.DEFAULT_DIST, False

    count_cc = 0
    for v in g.vertices:
        if not v.visited:
            count_cc += 1
            g.bfs(v)
    return count_cc
