def sort_square(lst, n):
    """
    Sort an array of integers that are in range - [0,n^2-1]
                Time complexity - O(n)
    :param lst: list of integers
    :param n: len of lst
    :return: new sorted array
    """

    diff_lst = [(0, 0)] * n
    for i in range(n):
        diff_lst[i] = (lst[i] % 10, lst[i] // 10)

    # TODO : radix sort on the list of tuples.

    sorted_list = [(num * 10) + deg for deg, num in diff_lst]
    return sorted_list
