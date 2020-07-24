from Data_Structures.MyGraph import *
from Data_Structures.UnionFind import *
from Algorithms.ArraySortAlgorithms import quick_sort


def kruskal(g, w):
    """
    Function that return the MST in g (graph).
    Find the MST by kruskal algorithm
                Time complexity : O(|E|*log(|E|))
    :param g: Undirected connected graph
    :param w: weights function
    :return: G that is MST of g. (V,E)
    """
    mst_edges = set()
    s = g.get_set_of_edges()
    # List of edges with their weight.
    weighted_edges = [(edge, w(edge)) for edge in s]
    # TODO
    #  quick_sort(weighted_edges) by the second index

    uf = UnionFind(g.vertices)
    for edge in weighted_edges[0]:
        if uf.find(edge[0]) == uf.find(edge[1]):
            mst_edges.add(edge)
            uf.union(edge[0], edge[1])
    return mst_edges


def prim(g, w):
    """
    Function that return the MST in g (graph).
    Find the MST by prim algorithm
                Time complexity : O((|V|+|E|)*log(|E|))

    :param g: Undirected connected graph
    :param w: weights function
    :return: G that is MST of g. (V,E)
    """

    # TODO
