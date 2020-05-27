from doubly_linked_list import *


class MyStack():
    """
    Stack class
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def push(self, item):
        """
        Insert new item to stack.
        :param item:
        :return:
        """
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev, self.head.next = self.head, new_node
            self.head = new_node

        self.len += 1

    def pop(self):
        """
        Pop out the last item in the stack
        :return:
        """
        if self.isStackEmpty():
            raise Exception("Can't Pop empty stack")

        else:
            ret = self.head.data
            self.head = self.head.prev
            self.len -= 1
            if not self.isStackEmpty():
                self.head.next = None

            return ret

    def isStackEmpty(self):
        """
        Check if the stack is empty.
        :return:
        """
        return not self.len


