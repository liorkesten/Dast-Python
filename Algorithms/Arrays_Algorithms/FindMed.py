from Algorithms.Sorting_Algorithms.Linear_Sorting.BinSort import *


def findMed(lst):
    """
    Gets an array and return the med item in the array
    :param lst: Array
    :return: med item in array lst
    """
    # Prevent circular imports!!!!

    if not lst:
        return
    m = findMax(lst)
    sorted_a = binSort(lst, m)
    return sorted_a[len(lst) // 2]
