from random import randint


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


def rand_partition(lst, s, e, piv_index=-1):
    """
    Rand partition - generate a random pivot and partition the array.
    :param a: array
    :param s: start index
    :param e: end index
    :param piv_index: (at a[e] is the pivot.
    :return: The index of the pivot
    """
    # Generate pivot.
    pivot_index = randint(s, e)
    lst[e], lst[pivot_index] = lst[pivot_index], lst[e]  # Swap.
    return partition(lst, s, e, piv_index)


def partition(a, s, e, piv_index=-1):
    """
    Partition - the pivot is the last item in the array.
    set all smaller items from left to the pivot and all greater right to pivot
    return the index of pivot.
    :param a: array
    :param s: start index
    :param e: end index
    :param piv_index: (at a[e] is the pivot.
    :return: The index of the pivot
    """
    pivot = a[piv_index]
    i = s
    for j in range(s, e):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1

    a[i], a[e] = a[e], a[i]
    return i  # Return pivot index


