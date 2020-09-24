from random import randint


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
