from .BinSort import *

# ________________________________Linear Sorts________________________________
BASIS_OF_RADIX_SORT = 10


def radixSort(A, d):
    """
    Function that gets an array of int numbers, and d that is the num of digits
    of the max value in d.
    :param A: Array of int nums
    :param d: num of digits of the maximum number.
    :return: New Sorted array of A.
    """
    # TODO - wait to counting sort - TA 8.
    ret = A[::]
    for i in range(1, d + 1):
        bin = [0] * BASIS_OF_RADIX_SORT
        ret = binSort(ret)
    pass
