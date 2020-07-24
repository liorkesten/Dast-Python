from Algorithms.Sort.QuickSort import rand_partition


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


def findMed(lst):
    """
    Gets an array and return the med item in the array
    :param lst: Array
    :return: med item in array lst
    """
    # Prevent circular imports!!!!
    from Algorithms.Sort.LinearSort.LinearSort import binSort

    if not lst:
        return
    m = findMax(lst)
    sorted_a = binSort(lst, m)
    return sorted_a[len(lst) // 2]


def quick_select(A, k, s=0, e=-1):
    """
    Find the k^th element in A. using partition.
                    Time Complexity : Worst case - O(n^2)
                                        Avg case: - O(n)
    :param A: Array of numbers.
    :param k: The k^th element
    :param s: Start index
    :param e: End index
    :return:
    """
    if e == -1:
        e = len(A) - 1

    p = rand_partition(A, s, e, e)

    if p == k - 1:  # p is the pivot.
        return A[p]
    elif p > k - 1:  # the k^th element is smaller than the pivot
        return quick_select(A, k, s, p - 1)
    else:  # the k^th element is greater than the pivot
        return quick_select(A, k, p + 1, e)


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


def is_arithmetic_progression(lst):
    """
    Check if there is a 3 numbers that are arithmetic_progression.
    for example -  [9,4,1,2] return False because there is not a sequence.
                    [4,2,7,1] return True because there is 1,4,7 are sequence.

    :param lst: lst of diff integers
    :return: True or False if there is a 3 sequence in the lst.
    """
    set_of_values = set(lst)
    # Check if there is 3 monotony
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            third_num = abs(lst[i] - lst[j]) + max(lst[i], lst[j])
            if third_num in set_of_values:
                return True

    return False
