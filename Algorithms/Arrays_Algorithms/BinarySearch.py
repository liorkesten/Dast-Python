def binary_search_array(lst, x):
    """
    Get a sorted list in search if x is in the array - return true or false.
                        Time Complexity O(log(n))
    :param lst: Sorted lst
    :param x: item to find
    :return: True or False if x is in the array
    """
    if not lst:
        return False
    if len(lst) == 1:
        return x == lst[0]
    mid = len(lst) // 2
    if lst[mid] == x:
        return True
    elif lst[mid] < x:
        return binary_search_array(lst[mid + 1:], x)
    elif lst[mid] > x:
        return binary_search_array(lst[:mid], x)