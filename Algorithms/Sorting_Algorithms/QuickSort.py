from Algorithms.Arrays_Algorithms.Partition import rand_partition


# _____________________________Random sorting_________________________________


def quick_sort(lst, s=0, e=-1):
    """
    Quick Sorting_Algorithms - Random pivot.
                Time complexity  - n*log(n) in the avg case.
                                    n^2 in the worst case.
    :param a: array
    :param s: start index
    :param e: end index
    :return: None - change the origin array.
    """
    # change e to the len of a.
    if e == -1:
        e = len(lst) - 1

    if s >= e:
        return

    p = rand_partition(lst, s, e)
    # Recursive calls
    quick_sort(lst, p + 1, e)  # Recursive right
    quick_sort(lst, s, p - 1)  # Recursive left
