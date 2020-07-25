from Algorithms.Arrays_Algorithms.FindMax import findMax
from Algorithms.Sorting_Algorithms.Linear_Sorting.BinSort import binSort


def findMed(lst):
    """
    Gets an array of integers that is bounded by some m - maximum integer
    The function return the med item in the array.
    :param lst: Array
    :return: med item in array lst
    """
    # Prevent circular imports!!!!

    if not lst:
        return
    m = findMax(lst)
    sorted_a = binSort(lst, m)
    return sorted_a[len(lst) // 2]
