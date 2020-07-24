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

    def is_bipartite(self):
        for v in self.vertices:
            v.side, v.visited = None, False

        for v in self.vertices:
            if v.visited: continue
            v.visited, v.side, v.parent = True, self.LEFT_SIDE, None
            q = MyQueue()
            q.enqueue(v)
            while not q.is_queue_empty():
                u = q.dequeue()
                cur = u.neighbors.head
                while cur:
                    # Undirected graph - of {x.y} so {y,x}
                    if cur.data == u.parent:
                        cur = cur.next
                        continue
                    # If the side is the same:
                    elif cur.data.side == u.side:
                        return False
                    if not cur.data.visited:
                        cur.data.visited, cur.data.side, cur.data.parent = \
                            True, not u.side, u
                        q.enqueue(cur.data)
                    cur = cur.next
        return True

    def has_cycles(self):
        """
        Check if there is cycles in the graph!
                            Time Complexity : O(|V|+|E|)
        :return: True or false if there is cycle in the graph
        """
        # Init the relevant attributes of all vertices
        for vertex in self.vertices:
            vertex.parent, vertex.visited = None, False
        # Check every vertex - maybe there is more than 1 CC.
        for v in self.vertices:
            if v.visited: continue
            v.visited = True
            q = MyQueue()
            q.enqueue(v)

            while not q.is_queue_empty():
                u = q.dequeue()
                cur = u.neighbors.head
                while cur:
                    # Undirected graph - of {x.y} so {y,x}
                    if cur.data == u.parent:
                        cur = cur.next
                        continue
                    # If the vertex already visited there is a cycle
                    elif cur.data.visited:
                        return True
                    else:
                        cur.data.visited, cur.data.parent = True, u
                        q.enqueue(cur.data)
                    cur = cur.next
        return False

    def cc(self):
        """
        Function that counting the comp connectivity in the graph and return
         the num of them
                                 Time Complexity : O(|V|+|E|)
        :return:
        """
        # Reset the dist and visited of each vertex
        for vertex in self.vertices:
            vertex.dist, vertex.visited = self.DEFAULT_DIST, False

        count_cc = 0
        for v in self.vertices:
            if not v.visited:
                count_cc += 1
                self.bfs(v)
        return count_cc

    def bfs(self, s):
        """
        BFS algorithm
                        Time Complexity : O(|V|+|E|)
        :param s:
        :return:
        """
        s.visited = True
        q = MyQueue()
        q.enqueue(s)
        while not q.is_queue_empty():
            u = q.dequeue()
            cur = u.neighbors.head
            while cur:
                if not cur.data.visited:
                    cur.data.visited, cur.data.dist = True, u.dist + 1
                    q.enqueue(cur.data)
                cur = cur.next

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
