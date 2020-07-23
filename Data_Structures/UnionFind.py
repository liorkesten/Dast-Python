from Data_Structures.my_doubly_linked_list import *


class UnionFind(set):
    """
    Class UnionFind.
    """
    def __init__(self, lst):
        super().__init__()
        self.__values_to_nodes = dict()
        self.make_all_sets(lst)

    def make_all_sets(self, lst):
        """
        create n linked lists.
        :param lst: lst of values
        :return: None
        """
        for key in lst:
            self.make_set(key)

    def make_set(self, key):
        """
        Create new set- create new linked list and
        :param key:
        :return:
        """
        new_linked_list = MyLinkedList()
        new_linked_list.push(key)
        self.__values_to_nodes[key] = new_linked_list.head
        # Set represent item
        new_linked_list.head.representative = new_linked_list
        # Add the linked list to the UnionFind obj.
        self.add(new_linked_list)

    def union(self, x, y):
        """
        Union 2 sets
        :param x:
        :param y:
        :return:
        """
        l1, l2 = self.find(x), self.find(y)
        # If the sets already union.
        if l1 is l2:
            return

        if l1.len > l2.len:
            self.union_helper(l1, l2)
        else:
            self.union_helper(l2, l1)

    def union_helper(self, longer, shorter):
        # Union lists
        longer.tail.next, shorter.head.prev = shorter.head, longer.tail
        # Update representative item:
        cur = shorter.head
        for i in range(shorter.len):
            cur.representative = longer
            cur = cur.next
        # Update tail and counter
        longer.tail = shorter.tail
        longer.len += shorter.len

        # remove shorter from set.
        self.remove(shorter)

    def find(self, x):
        """
        Find the representative item of x.
        :param x: node
        :return:
        """
        try:
            return self.__values_to_nodes[x].representative
        except SyntaxError:
            raise Exception(f"{x} doesnt have a representative item")
