
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

