from Algorithms.Sorting_Algorithms.QuickSort import *


def quick_select(A, k, s=0, e=-1):
    """
    Find the k^th element in A. using partition.
                    Time Complexity : Worst case - O(n^2)
                                        Avg case: - O(n)
    :param A: Array of numbers.
    :param k: The k^th element
    :param s: Start index
    :param e: End index
    :return:
    """
    if e == -1:
        e = len(A) - 1

    p = rand_partition(A, s, e, e)

    if p == k - 1:  # p is the pivot.
        return A[p]
    elif p > k - 1:  # the k^th element is smaller than the pivot
        return quick_select(A, k, s, p - 1)
    else:  # the k^th element is greater than the pivot
        return quick_select(A, k, p + 1, e)
