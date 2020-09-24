from Data_Structures.MaxHeap import *


def print_max(H, k):
    """
    Gets an heap and k, and print the k^th biggest numbers in the heap
    in descending order.
                            Time complexity : O(klog(k))
    :param H: MaxHeap
    :param k: integer < size(heap)
    :return: None - print values.
    """
    # TODO
    new_heap = MaxHeap()
    ans = [] * k
    # new_heap.insert(H.)
