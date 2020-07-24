from Data_Structures.MyQueue import *
from Data_Structures.my_doubly_linked_list import *


class Vertex:
    def __init__(self, data=None, neighbors=None):
        self.data = data
        self.neighbors = neighbors
        self.dist = 0
        self.visited = False

    def __str__(self):
        return str(self.data)


class MyGraph:
    """
    Graph object:
    List of vertices.
    each item in vertices is a vertex that has all his neighbors in a linked
    list
    #TODO Build Graph
    """
    DEFAULT_DIST = 0
    LEFT_SIDE = False
    RIGHT_SIDE = True

    def __init__(self, vertices=[]):
        self.vertices = vertices

    def display(self):
        for v in self.vertices:
            print(f"[{v}]--->", end="")
            cur = v.neighbors.head
            while cur:
                print(f"{cur}-->", end="")
                cur = cur.next
            print("")

    def get_set_of_edges(self):
        set_of_edges = set()
        for vertex in self.vertices:
            for neighbor in vertex.neighbors:
                if (vertex.data, neighbor) in set_of_edges or \
                        (neighbor, vertex.data) in set_of_edges:
                    continue
                else:
                    set_of_edges.add((vertex.data, neighbor))
        return set_of_edges
