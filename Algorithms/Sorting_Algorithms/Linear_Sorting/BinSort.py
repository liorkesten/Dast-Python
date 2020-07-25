def binSort(A, m):
    """
    Bin Sorting_Algorithms - algorithm: gets an array of int numbers, find the maximum value
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
    ret = [0] * len(A)

    j = 0  # Index of ret Array
    for i in range(m + 1):
        for k in range(bins[i]):
            ret[j] = i
            j += 1

    return ret
