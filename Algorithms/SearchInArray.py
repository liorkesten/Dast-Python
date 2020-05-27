def find(A, x):
    """
    Function that gets a List and item x and return True or False if the item
    is  in the list.
                            Complexity Time - O(n)
    :param A: Array
    :param x: item to find
    :return: True or False if x is in the array
    """
    for item in A:
        if x == item:
            return True
    return False


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


def findMed(A):
    """
    Gets an array and return the med item in the array
    :param A: Array
    :return: med item in array A
    """
    # Prevent circular imports!!!!
    from Algorithms.LinearSort import binSort

    if not A:
        return
    m = findMax(A)
    sorted_A = binSort(A, m)
    return sorted_A[len(A) // 2]


def quickSelect(A, k):
    # TODO implement
    pass


def findMax(A):
    """
    Get array and return the max item in the array
    :param A:
    :return: maximum value  in the array, -inf if the array is empty.
    """
    maximum = float("-inf")
    for item in A:
        if maximum < item:
            maximum = item

    return maximum
