def binary_search_array(lst, x):
    """"""
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
    # TODO implement findMed using TA 7
    pass


def quickSelect(A, k):
    # TODO implement
    noam = 0
    pass
