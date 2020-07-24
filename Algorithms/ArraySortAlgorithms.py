"""
Array Sort Algorithms:
1. Merge Sort
2. Selection Sort
"""
from Data_Structures.MinHeap import *
from random import randint


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


# _______________________________Determinist sorting__________________________

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


def insertion_sort(lst):
    """
    Insertion Sort- goes from a[0] to a[-1] and each iteration sort
    the sub array.
                    Time complexity - O(n^2)
    :param lst: list
    :return:
    """
    for i in range(1, len(lst)):
        j = i
        # checks if a[j-1]<a[
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1


# _____________________________Random sorting_________________________________
def quick_sort(lst, s=0, e=-1):
    """
    Quick Sort - Random pivot.
                Time complexity  - n*log(n) in the avg case.
                                    n^2 in the worst case.
    :param a: array
    :param s: start index
    :param e: end index
    :return: None - change the origin array.
    """
    # change e to the len of a.
    if e == -1:
        e = len(lst) - 1

    if s >= e:
        return

    p = rand_partition(lst, s, e)
    # Recursive calls
    quick_sort(lst, p + 1, e)  # Recursive right
    quick_sort(lst, s, p - 1)  # Recursive left


def rand_partition(lst, s, e, piv_index=-1):
    """
    Rand partition - generate a random pivot and partition the array.
    :param a: array
    :param s: start index
    :param e: end index
    :param piv_index: (at a[e] is the pivot.
    :return: The index of the pivot
    """
    # Generate pivot.
    pivot_index = randint(s, e)
    lst[e], lst[pivot_index] = lst[pivot_index], lst[e]  # Swap.
    return partition(lst, s, e, piv_index)


def partition(a, s, e, piv_index=-1):
    """
    Partition - the pivot is the last item in the array.
    set all smaller items from left to the pivot and all greater right to pivot
    return the index of pivot.
    :param a: array
    :param s: start index
    :param e: end index
    :param piv_index: (at a[e] is the pivot.
    :return: The index of the pivot
    """
    pivot = a[piv_index]
    i = s
    for j in range(s, e):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1

    a[i], a[e] = a[e], a[i]
    return i  # Return pivot index


