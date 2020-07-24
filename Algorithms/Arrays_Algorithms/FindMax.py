
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