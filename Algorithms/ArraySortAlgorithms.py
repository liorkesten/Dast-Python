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

def findMax(A):
    """
    Get array and return the max item in the array
    :param A:
    :return: maximum value  in the array, -inf if the array is empty.
    """
    maximum = float("-inf")
    for item in A:
        if maximum < item:
            maximum = item

    return maximum


def binSort(A):
    """
    Bin Sort - algorithm: gets an array of int numbers, find the maximum value
     (m) in the array, than create an list of [0,1,...,m] and than increase
     the counter of the A array. Put the amount of each index in
     ret array and return ret
    :param A: array of int nums
    :return: new Array that is sorted.
    """
    m = findMax(A)
    if m == float("-inf"):
        return []
    # Define bins in len m+1 because m is the max value so bins[0]=0,
    # bins[m+1]=m
    bins = [0] * (m + 1)
    for index in A:
        bins[index] += 1
    # Init the return value arr
    ret = [None] * len(A)

    j = 0  # Index of ret Array
    for i in range(m + 1):
        for k in range(bins[i]):
            ret[j] = i
            j += 1

    return ret


def radixSort(A, d):
    # TODO implement radixSort
    pass


binSort([1])
