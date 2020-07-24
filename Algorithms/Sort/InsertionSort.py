
def insertion_sort(lst):
    """
    Insertion Sort- goes from a[0] to a[-1] and each iteration sort
    the sub array.
                    Time complexity - O(n^2)
    :param lst: list
    :return:
    """
    for i in range(1, len(lst)):
        j = i
        # checks if a[j-1]<a[
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1