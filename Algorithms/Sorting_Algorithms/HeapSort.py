from Data_Structures.MinHeap import MinHeap


def heap_sort(lst):
    """
    Sorting_Algorithms by creating Min Heap and than extract all items to to origin list.
                    Time Complexity -  O(nlog(n))

    :param lst:
    """
    new_heap = MinHeap(lst)

    # Extract all items in ascending order to a list.
    for i in range(len(lst)):
        lst[i] = new_heap.extract_min()