class Node():
    def __init__(self, data=None, parent=None, left_child=None,
                 right_child=None):
        self.data = data
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        # For OrderStat algorithm
        self.num_vertices_left = 0

    def is_leaf(self):
        return not self.left_child and not self.right_child

    def __str__(self):
        return str(self.data)


class Bst:
    def __init__(self, array=[]):
        self.root = None
        self.n = 0

        self.build_bst(array)

    # __________________________________ QUERIES _____________________________

    def build_bst(self, array):
        if not array:
            return
        for val in array:
            self.insert(val)

    def insert(self, new_value):
        if self.find(new_value):  # check if the value already exist in the bst
            return

        new_node = Node(new_value)
        if not self.root:
            self.root = new_node

        else:
            cur = self.root
            while True:
                if cur.data < new_value:
                    if not cur.right_child:
                        cur.right_child, new_node.parent = new_node, cur
                        break
                    else:
                        cur = cur.right_child
                else:
                    if not cur.left_child:
                        cur.left_child, new_node.parent = new_node, cur
                        break
                    else:
                        cur = cur.left_child
            self.n += 1

        return new_node

    def find(self, x):
        """
        Find in bst
                        Time Complexity - O(h) : h is the height of the tree
        :param x: value of some node
        :return: The node of x if the x (value) is in the tree, else None
        """
        cur = self.root
        while cur:
            if cur.data == x:
                return cur

            elif cur.data < x:
                cur = cur.right_child
            else:
                cur = cur.left_child
        return None

    def find_min(self, root=None):
        if not root:
            root = self.root
        cur = root
        if not cur:
            raise Exception("Find max in empty bst doesnt work!")

        while cur.left_child:
            cur = cur.left_child

        return cur

    def find_max(self, root=None):
        """
        Find the max value in the tree and return it
        :param root: root of the tree
        :return: The node with the max value of the tree
        """
        if not root:
            root = self.root
        cur = root
        if not cur:
            raise Exception("Find max in empty bst doesnt work!")

        while cur.right_child:
            cur = cur.right_child

        return cur

    def successor(self, x):
        """
        Return the node of the successor of node x
        :param x: Node in the bst
        :return: Node of the successor of x.
        """
        if not x:
            raise Exception("Must insert valid pointer")
        if x.right_child:
            return self.find_min(x.right_child)

        else:
            cur = x
            while cur.parent:
                if cur.parent.left_child and cur == cur.parent.left_child:
                    return cur.parent
                else:
                    cur = cur.parent

    def predecessor(self, x):
        if not x:
            raise Exception("Must insert valid pointer")
        if x.left_child:
            return self.find_max(x.left_child)

        else:
            cur = x
            while cur.parent:
                if cur.parent.right_child and cur == cur.parent.right_child:
                    return cur.parent
                else:
                    cur = cur.parent

    def delete(self, x):
        """
        Delete from Tree
        :param x: x (value) to deleted.
        :return: None - only delete
        """
        cur = self.find(x)
        if not cur:
            raise Exception(f"The value {x} is not in the tree")
        else:
            # if the cur is leaf:
            if cur.is_leaf():
                self._delete_no_children(cur)
            # if the cur has only 1 child:
            elif not cur.left_child:
                self._delete_only_one_child(cur, cur.right_child)
            elif not cur.right_child:
                self._delete_only_one_child(cur, cur.left_child)
            # if the cur has 2 children:
            else:
                self._delete_two_children(cur)
            self.n -= 1

    def _delete_no_children(self, cur):
        """
        Delete case that the node cur has no children
        :param cur: node to delete
        :return: None
        """
        # Delete the pointer of the parent to cur.
        if cur.parent:
            if cur.parent.left_child == cur:
                cur.parent.left_child = None
            else:
                cur.parent.right_child = None
        # In case that cur is the root of the BST.
        else:
            self.root = None

    def _delete_only_one_child(self, cur, child):
        """
        Delete case if cur has 1 child
        :param cur: node to delete
        :param child: The child of cur
        :return: None
        """
        if cur.parent:
            # Switch Pointers of cur child and cur parent
            # A-> B-> C       A -> C
            if cur.parent.right_child == cur:
                cur.parent.right_child, child.parent = child, cur.parent
            else:
                cur.parent.left_child, child.parent = child, cur.parent
        # if cur is the root
        else:
            self.root = child
            self.root.parent = None

    def _delete_two_children(self, cur):
        """
        Delete case if cur has 2 children - Switch the values of cur and
        cur.successor.
        Cur successor can have only 1 child or zero.
        :param cur: node to delete
        :return: None
        """
        suc = self.successor(cur)
        cur.data = suc.data
        # if cur has 2 children, than its successor can have only 1 child
        # (or zero).
        if suc.is_leaf():
            self._delete_no_children(suc)
        else:
            self._delete_only_one_child(suc, suc.right_child)

    #  ______________________ Print BST _______________________________________
    def print_bst(self, reverse=False):
        """
        Print BST in order - with out graphic.
        Recursive version
        :param reverse: True or False to print in reverse order
        :return: None - only printing the tree
        """
        if not reverse:
            self._print_bst_in_order(self.root)
        else:
            self._print_bst_in_reverse_order(self.root)

    def _print_bst_in_order(self, root: Node) -> None:
        """
        Print BST in recursive in order from the smallest to the biggest
        :param root: root of the tree
        """
        if root:
            # Left
            self._print_bst_in_order(root.left_child)
            # Parent
            print(root)
            # Right
            self._print_bst_in_order(root.right_child)

    def print_bst_with_successor(self):
        """
        Print the values in the bst in order - iteration version
        (not recursive).
        :return: None - only print the values in the tree in ascending order.
        """
        cur = self.find_min(self.root)
        while cur:
            print(cur.data)
            cur = self.successor(cur)

    def _print_bst_in_reverse_order(self, root):
        """
        Print BST in recursive in reverse order from the biggest to the
        smallest
        :param root: root of the tree
        """
        if root:
            self._print_bst_in_reverse_order(root.right_child)
            print(root)
            self._print_bst_in_reverse_order(root.left_child)

    def display(self):
        current_level = [self.root]
        if not current_level:
            return
        while current_level:
            print(' '.join(str(node) for node in current_level))
            next_level = list()
            for n in current_level:
                if n and n.left_child:
                    next_level.append(n.left_child)
                if n and n.right_child:
                    next_level.append(n.right_child)
            current_level = next_level

# a = [4, 6, 2, 1, 5, 7, 3]
# a = [15, 5, 16, 3, 12, 10, 6, 7, 13, 16, 20]
# new_bst = Bst(a)
# new_bst.print_bst_with_successor()
# new_bst.display()
# print(new_bst.successor(new_bst.root.left_child.right_child))
# # print(new_bst.predecessor(new_bst.root))
# # new_bst.delete(7)
# print("_" * 30)
# new_bst.print_bst(reverse=True)
# new_bst.delete(5)
# print("_" * 30)
# new_bst.display()
# # print(new_bst.find_max())
# # print(new_bst.find_min())
