from Data_Structures.Bst import *
from Algorithms.Sort import MergeSort
import math


class Node():
    def __init__(self, data=None, height=None, balance="=", left_sum=0,
                 parent=None, left_child=None, right_child=None):
        self.data = data
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

        self.height = height
        self.balance = balance
        self.left_sum = left_sum

    def __str__(self):
        return str(self.data)


class Avl(Bst):
    def __init__(self, array=[], sorted=False):
        Bst.__init__(self, None)
        if sorted:
            self.root = self.build_avl_sorted_list(array)
        else:
            self.build_avl_no_sorted_list(array)

    def build_avl_sorted_list(self, array):
        """
        Build AVL tree from sorted list - recursively create a left node,
        node, right node - Similar to print_BST_in_order
                        Time Complexity: O(n): T(n)=2T(n/2)+O(1)
        :param array:
        :return:
        """
        if not array:
            return None
        elif len(array) == 1:
            return Node(array[0], height=0, left_sum=array[0])
        else:
            mid = math.ceil(len(array) // 2)  # Round up mid
            # Algorithm for building AVL
            x = Node(array[mid], left_sum=array[mid])
            x.left_child = self.build_avl_sorted_list(array[:mid])
            x.right_child = self.build_avl_sorted_list(array[mid + 1:])
            # Init left sum, height, and balance:
            self._set_left_sum(x)
            self._set_balance(x, x.left_child, x.right_child)
            self._set_height(x, x.left_child, x.right_child)
            # Init Parents
            if x.left_child:
                x.left_child.parent = x
            if x.right_child:
                x.right_child.parent = x
            return x

    def build_avl_no_sorted_list(self, array):
        for val in array:
            self.insert_avl(val)

    def insert_avl(self, val):
        node = self.insert(val)  # insert BST method
        if not node:
            raise Exception("val is already in the tree")
        # Update nodes values
        self.update_tree_after_insert(node)

    def update_tree_after_insert(self, node):
        while node:
            self._set_height(node, node.left_child, node.right_child)
            delta = self._get_delta(node.left_child, node.right_child)
            self.rotate(node, delta)
            self._set_left_sum(node)
            self._set_balance(node, node.left_child, node.right_child)
            node = node.parent

    def rotate(self, x, delta):
        if delta == 2:
            if x.left_child.balance == ">" or x.left_child.balance == "=":
                self.ll_rotate(x)
            elif x.left_child.balance == "<":
                self.lr_rotate(x)

        elif delta == -2:
            if x.right_child.balance == "<" or x.right_child.balance == "=":
                self.rr_rotate(x)
            elif x.right_child.balance == ">":
                self.rl_rotate(x)

        else:  # the tree is balanced!
            return

    def right_rotate(self, x):
        pass

    def left_rotate(self, x):
        if x is not self.root:
            # if x is the left child of his parent
            if x.parent.left_child == x:
                x.parent.left_child, x.right_child.parent = \
                    x.right_child, x.parent
        pass

    def ll_rotate(self, node):
        self.right_rotate(node)

    def rl_rotate(self, node):
        self.right_rotate(node)
        self.left_rotate(node)

    def rr_rotate(self, node):
        self.left_rotate(node)

    def lr_rotate(self, node):
        self.left_rotate(node)
        self.right_rotate(node)

    def _get_delta(self, left, right):
        if left and right:
            return left.height - right.height
        elif left:
            return left.height + 1
        elif right:
            return right.height - 1
        else:
            return None

    def _set_left_sum(self, x):
        x.left_sum = x.data
        if x.left_child:
            x.left_sum += x.left_child.left_sum
            if x.left_child.right_child:
                x.left_sum += x.left_child.right_child.left_sum

    def _set_height(self, x, left, right):
        # if x has 2 children
        if left and right:
            x.height = max(left.height, right.height) + 1
        # if x doesnt have children
        elif not left and not right:
            x.height = 0
        # if x has only left child
        elif left:
            x.height = left.height + 1
        # if x has only right child
        else:
            x.height = right.height + 1

    def _set_balance(self, x, left, right):
        # if x has 2 children
        if left and right:
            x.balance = \
                "=" if right.height == left.height \
                    else ">" if left.height > right.height \
                    else "<"
        # if x doesnt have children
        elif not left and not right:
            x.balance = "="
        # if x has only left child
        elif left:
            x.balance = ">"
        # if x has only right child
        else:
            x.balance = "<"


# a = [4, 6, 2, 1, 5, 7, 3]
# a = [15, 5, 3, 12, 10, 6, 7, 13, 16, 20]
a = [4, 6]
sorted_a = MergeSort.mergeSort(a)
new_bst = Avl(sorted_a, True)
new_bst.display()
print("_" * 30)
print(new_bst.insert_avl(2))
print("_" * 30)
new_bst.display()
