from Data_Structures.MyQueue import *


def is_bipartite(g):
    """
    Checks if the graph is bipartite.
                Time complexity - O(|V|+|E|)
    :param g: graph
    :return: True or False if the graph is bipartite
    """
    for v in g.vertices:
        v.side, v.visited = None, False

    for v in g.vertices:
        if v.visited: continue
        v.visited, v.side, v.parent = True, g.LEFT_SIDE, None
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
