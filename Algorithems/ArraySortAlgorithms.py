"""
Array Sort Algorithms:
1. Merge Sort
2. Selection Sort
"""


# ________________________________Sorts without assumption on A________________
def mergeSort(lst):
    """
    Merge Sort algorithm: gets an array sort it by mergeSort algorithm
                     Time complexity: nlog(n)
    :param lst:
    :return:
    """
    if not lst: return
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])
    return _merge(left, right)


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
        elif i >= len(lstA):
            lstC.append(lstB[j])
            j += 1
        elif j >= len(lstB) or lstA[i] <= lstB[j]:
            lstC.append(lstA[i])
            i += 1
        else:
            lstC.append(lstB[j])
            j += 1
    return lstC


# ___________________________________________________________________________


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
    for i, item in enumerate(lst[:last]):
        if item > lst[max_item_index]:
            max_item_index = i

    lst[last - 1], lst[max_item_index] = lst[max_item_index], lst[last - 1]
    selection_sort(lst, last - 1)


# ________________________________Linear Sorts________________________________

def binSort(A):
    # TODO implement binSort using FindMax (implement too)
    pass


def radixSort(A, d):
    # TODO implement radixSort
    pass
