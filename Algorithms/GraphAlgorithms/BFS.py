from Data_Structures.MyQueue import *


def bfs(s):
    """
    BFS algorithm
                    Time Complexity : O(|V|+|E|)
    :param s: start node at undirected graph
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
