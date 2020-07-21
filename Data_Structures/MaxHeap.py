from collections import deque
from Data_Structures.MyHeap import *

class MaxHeap(MyHeap):
    """
    Max heap object:
    Extract Max - O(1)
    Build Heap - O(n)
    Insert - O(log(n))
    Delete - O(log(n))
    """
    def __init__(self, array=[]):
        MyHeap.__init__(self, array)
        self.build_heap(array)

    # _________________________Build Heap______________________________________
    def build_heap(self, array):
        """
        Build max_heap:
        Step 1: -- Build random heap from list (Heap method)
        Step 2: use build_heap_helper:
            recursively build helper left child and after right child
            and than heapifyDown x
                    Time Complexity: O(n)
        :param array: array
        :return:
        """
        # self.build_random_heap(array) # In the algo this is the first step
        self.build_heap_helper(self.root)

    def build_heap_helper(self, x):
        if not x:
            return
        self.build_heap_helper(x.left_child)
        self.build_heap_helper(x.right_child)
        self.HeapifyDown(x)

    # _________________________Queries______________________________________
    def insert(self, new_value):
        """
        Insert new
        :param new_value:
        :return:
        """
        new_nth = self.add_node(new_value)
        self.HeapifyUp(new_nth)

    def find_max(self):
        """
        Function that return the maximum value in the heap - located in the
        root
        :return:
        """
        return self.root.data

    def extract_max(self):
        """
        Pop out the maximum value in the heap and fix the heap property.
        Step 1: save the value of the maximum.
        Step 2: Delete the nth node and put the nth.value in root.
        Step 3: HeapifyDown to root to save the heap property
        Step 4: return max value
        :return:
        """
        ret = self.root.data
        nth_data = self.delete_nth_node()
        self.root.data = nth_data
        self.HeapifyDown(self.root)
        return ret

    def delete_node(self, x):
        """
        Gets an pointer to node in heap and delete this node.
        :param x:
        :return:
        """
        if not x:
            raise Exception("Must insert node for delete")

        nth = self.get_nth_node()
        if not nth:
            raise Exception("Can't delete empty heap")

        nth.data, x.data = x.data, nth.data  # swap values
        self.delete_nth_node()

        if x.parent and x.data > x.parent.data:
            self.HeapifyUp(x)
        else:
            self.HeapifyDown(x)

    # _________________________Tools__________________________________________

    def HeapifyDown(self, x):
        """
        Bubbling the x.data until the heap is saving the property heap.
                    time Complexity log(n)
        :param x:
        :return:
        """
        if not x:
            return
        # if there is 2 children
        if x.left_child and x.right_child:
            if x.data >= x.left_child.data and x.data >= x.right_child.data:
                return
            elif x.left_child.data >= x.right_child.data:
                x.left_child.data, x.data = x.data, x.left_child.data
                return self.HeapifyDown(x.left_child)
            else:
                x.right_child.data, x.data = x.data, x.right_child.data
                return self.HeapifyDown(x.right_child)
        # if there is only left child:
        elif x.left_child and x.data < x.left_child.data:
            x.left_child.data, x.data = x.data, x.left_child.data
            self.HeapifyDown(x.left_child)
        # if there is only right child:
        elif x.right_child and x.data < x.right_child.data:
            x.right_child.data, x.data = x.data, x.right_child.data
            self.HeapifyDown(x.left_child)

    def HeapifyUp(self, x):
        """
        HeapifyUp algorithm -gets a pointer in heap that maybe the value of
        the node doesnt save the heap property and the algo bubbling the value
         of x in recursive until the correct node.
         after this algo the heap property saved.

                        time Complexity log(n)
        :param x:
        :return:
        """
        if x and x.parent and x.data > x.parent.data:
            x.parent.data, x.data = x.data, x.parent.data
            self.HeapifyUp(x.parent)

    def heap_sort(self):
        pass

heap = MaxHeap([5,1,333,42,1222,4,78,99,2])
heap.display()
print("_" * 20)
heap.insert(105)
heap.display()
print("_" * 20)
heap.delete_node(heap.root)
heap.display()
print("_" * 20)
print(heap.extract_max())
heap.display()
