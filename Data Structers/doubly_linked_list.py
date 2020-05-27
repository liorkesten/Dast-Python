class Node:
    """
    Class Node; simple node that has the basic fields.
    """
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class LinkedList:
    """
    Regular linked list
    """
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.len = 0

    def push(self, vertex):
        """
        Insert item to the linked list - make the new item as head of the list
        :param vertex:
        :return:
        """
        new_node = Node(vertex)
        if not self.head:
            self.head, self.tail = new_node, new_node
        else:
            new_node.next, self.head.prev = self.head, new_node
            self.head = new_node
        self.len += 1