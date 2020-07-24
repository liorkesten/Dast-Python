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