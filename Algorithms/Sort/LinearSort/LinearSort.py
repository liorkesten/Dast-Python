from Algorithms.SearchInArray import findMax

# ________________________________Linear Sorts________________________________
BASIS_OF_RADIX_SORT = 10


def binSort(A, m):
    """
    Bin Sort - algorithm: gets an array of int numbers, find the maximum value
     (m) in the array, than create an list of [0,1,...,m] and than increase
     the counter of the A array. Put the amount of each index in
     ret array and return ret
    :param m:
    :param A: array of int nums
    :return: new Array that is sorted.
    """
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
