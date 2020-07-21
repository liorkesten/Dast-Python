"""
Array Sort Algorithms:
1. Merge Sort
2. Selection Sort
"""
from Data_Structures.MinHeap import *


# ________________________________Sorts without assumption on A________________
def mergeSort(lst):
    """
    Merge Sort algorithm: gets an array sort it by mergeSort algorithm
                     Time complexity: n*log(n)
    :param lst:
    :return:
    """
    if not lst: return
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = mergeSort(lst[:mid])  # Recursive Left.
    right = mergeSort(lst[mid:])  # Recursive Right.
    return _merge(left, right)  # Merge 2 sorted lists


def _merge(lstA, lstB):
    """
    Merge function - get 2 sorted list and merge them to 1 sorted list
    :param lstA:
    :param lstB:
    :return: 1 Sorted list of lstA and lstB
    """
    lstC = []
    i, j = 0, 0
    while True:
        if i >= len(lstA) and j >= len(lstB):
            break
        # in case that all elements from a inserted to C
        elif i >= len(lstA):
            lstC.append(lstB[j])
            j += 1
        # In case that all elements from B inserted to C or B[j]>A[i]
        elif j >= len(lstB) or lstA[i] <= lstB[j]:
            lstC.append(lstA[i])
            i += 1
        # In case that A[i]>B[j]
        else:
            lstC.append(lstB[j])
            j += 1
    return lstC


# ___________________________________________________________________________

def heap_sort(lst):
    """
    Sort by creating Min Heap and than extract all items to to origin list.
                    Time Complexity -  O(nlog(n))

    :param lst:
    """
    new_heap = MinHeap(lst)

    # Extract all items in ascending order to a list.
    for i in range(len(lst)):
        lst[i] = new_heap.extract_min()



def selection_sort(lst, last):
    """
    Selection Sort.
                      Complexity Time: O(N^2)
    :param lst:
    :param last:
    :return:
    """
    if not last:  # Base Case
        return

    max_item_index = 0
    # Find the max item in the list and keep it index.
    for i, item in enumerate(lst[:last]):
        if item > lst[max_item_index]:
            max_item_index = i

    # Swtich the maximum with the last element
    lst[last - 1], lst[max_item_index] = lst[max_item_index], lst[last - 1]
    # Recursive call
    selection_sort(lst, last - 1)
