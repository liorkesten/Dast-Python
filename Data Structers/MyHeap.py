from collections import deque


class Node():
    def __init__(self, data=None, parent=None, left_child=None,
                 right_child=None):
        self.data = data
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child


class MyHeap():
    """
    Heap object: Tree with out any special ability.
    all heaps are heritage from this obj.
    """
    RIGHT_CHILD = "1"
    LEFT_CHILD = "0"

    def __init__(self, array=[]):
        self.root = None
        self.nth_binary_representing = ""
        self.n = 0
        self.build_random_heap(array)
        self.nth_binary_representing = format(len(array), "b")
        self.n = len(array)

    # _________________________Build Heap______________________________________
    def build_random_heap(self, array):
        """
        Function that creates a random heap - by indexes of array:
        array[i] -> left_child = array[2i], right_child = [2*i+1]
        :param array:
        :return: The root of the heap (Node obj)
        """
        nodes_list = [Node(i) for i in array]
        nodes_list.insert(0, None)

        for i in range(1, len(nodes_list)):
            if (2 * i) <= (len(nodes_list) - 1):
                nodes_list[i].left_child = nodes_list[2 * i]
                nodes_list[2 * i].parent = nodes_list[i]

            if ((2 * i) + 1) <= (len(nodes_list) - 1):
                nodes_list[i].right_child = nodes_list[(2 * i) + 1]
                nodes_list[(2 * i) + 1].parent = nodes_list[i]
        self.root = nodes_list[1]

    # _________________________Queries______________________________________

    def get_nth_node(self):
        """
        Function that travel in the heap by the binary representation of the
        nth node
        :return:  a pointer to nth node
        """
        cur = None
        for ch in self.nth_binary_representing:
            if ch == self.RIGHT_CHILD:
                if not cur:  # init for the first iteration
                    cur = self.root
                else:
                    cur = cur.right_child
            elif ch == self.LEFT_CHILD:
                cur = cur.left_child
        return cur

    # _________________________Tools__________________________________________

    def add_node(self, new_value):
        """
        Add one node to the heap and increase the nth and the
        nth_binary_representing
        :param new_value: 
        :return: 
        """
        self.n += 1
        self.nth_binary_representing = format(self.n, "b")

        cur = None
        for i in range(len(self.nth_binary_representing) - 1):
            if self.nth_binary_representing[i] == self.RIGHT_CHILD:
                if not cur:  # init for the first iteration
                    cur = self.root
                else:
                    cur = cur.right_child
            elif self.nth_binary_representing[i] == self.LEFT_CHILD:
                cur = cur.left_child

        if self.nth_binary_representing[-1] == self.LEFT_CHILD:
            cur.left_child = Node(new_value, cur)
            return cur.left_child
        elif self.nth_binary_representing[-1] == self.RIGHT_CHILD:
            cur.right_child = Node(new_value, cur)
            return cur.right_child

    def delete_nth_node(self):
        """
        Delete the nth node from the heap
        :return: 
        """
        nth_leaf = self.get_nth_node()
        if not nth_leaf:
            raise Exception("Can't delete empty heap")
        # The last should be the right child.

        if nth_leaf.parent.right_child:
            nth_leaf.parent.right_child = None
        else:
            nth_leaf.parent.left_child = None

        # update the nth
        self.n -= 1
        self.nth_binary_representing = format(self.n, "b")
        return nth_leaf.data

    def display(self):
        """
        Print heap function
        :return: 
        """
        buf = deque()
        output = []
        if not self.root:
            print('$')
        else:
            buf.append(self.root)
            count, nextCount = 1, 0
            while count:
                node = buf.popleft()
                if node:
                    output.append(node.data)
                    count -= 1
                    for n in (node.left_child, node.right_child):
                        if n:
                            buf.append(n)
                            nextCount += 1
                        else:
                            buf.append(None)
                else:
                    output.append('$')
                if not count:
                    print(output)
                    output = []
                    count, nextCount = nextCount, 0
            # print the remaining all empty leaf node part
            output.extend(['$'] * len(buf))
            print(output)
