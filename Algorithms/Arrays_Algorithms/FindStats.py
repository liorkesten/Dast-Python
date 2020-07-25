from Algorithms.Arrays_Algorithms.QuickSelect import *


def find_stats(lst, k):
    """
    Algorithm that gets an array of integers that 2^k<=n (len of lst) and
    return a list of all the k^th pows of 2 of the lst.
                    Time complexity : O(n)
    :param lst: lst of integers
    :param k: return k elements.
    :return:
    """
    ret = [0] * k
    ret[- 1] = quick_select(lst, (2 ** k) - 1, 0, len(lst) - 1)
    for i in range(k - 1, 0, -1):
        ret[i - 1] = quick_select(lst, (2 ** i)-1, 0, 2 ** (i + 1))

    return ret


print(find_stats(
    [2, 4, 4, 2, 3, 5, 1, 212, 243, 2424, 2424, 24242, 21, 1, 22, 4, 4, 444,
     42, 121, 124, 0], 4))
