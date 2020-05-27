from Data_Structers.my_doubly_linked_list import *


class MyQueue():
    """
    Queue: Fifo ds
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def enqueue(self, item):
        """
        Add item to the queue
        :param item:
        :return:
        """
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail
            self.tail.prev = new_node
            self.tail = new_node
        self.len += 1

    def dequeue(self):
        """
        Pop out the first item in the queue
        :return:
        """
        if self.is_queue_empty():
            raise Exception("Cant Dequeue when the Queue is empty")

        ret = self.head.data
        self.head = self.head.prev
        if self.head:
            self.head.next = None
        self.len -= 1
        return ret

    def is_queue_empty(self):
        """
        Check if the queue is empty
        :return:
        """
        return not self.len
