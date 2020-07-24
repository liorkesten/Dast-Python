from Data_Structures.MyQueue import *


def has_cycles(g):
    """
    Check if there is cycles in the graph!
                        Time Complexity : O(|V|+|E|)
    :return: True or false if there is cycle in the graph
    :param g:
    :return:
    """
    # Init the relevant attributes of all vertices
    for vertex in g.vertices:
        vertex.parent, vertex.visited = None, False
    # Check every vertex - maybe there is more than 1 CC.
    for v in g.vertices:
        if v.visited: continue
        v.visited = True
        q = MyQueue()
        q.enqueue(v)

        while not q.is_queue_empty():
            u = q.dequeue()
            cur = u.neighbors.head
            while cur:
                # Undirected graph.
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
