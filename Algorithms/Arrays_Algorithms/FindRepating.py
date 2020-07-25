from Algorithms.Arrays_Algorithms.QuickSelect import quick_select


def find_repeating(lst):
    """
    Gets an list and return if there is more than n/2 repeats on some val.
    :param lst: lst of integers
    :return: the n/2 element if there is one, else None
    """
    supposed = quick_select(lst, len(lst) // 2)
    counter_appears = 0
    for val in lst:
        if val == counter_appears:
            counter_appears += 1

    if counter_appears > len(lst) // 2:
        return supposed
    return None
