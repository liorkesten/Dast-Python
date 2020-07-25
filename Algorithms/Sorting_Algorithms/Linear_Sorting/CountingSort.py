def counting_sort(lst, m):
    """
    Sort array of integers in the range - 0-m.
    Stable sorting
                    Time complexity : O(n+m)
    :param lst: list of integers.
    :param m: maximum integer in lst
    :return: new sorted array.
    """
    # Create bins array - [0,m]
    bins = [0] * (m + 1)
    # Add values from lst to bins
    for item in lst:
        bins[item] += 1
    # Update values of bins - bins[i] += bins[i-1]
    for i in range(2, m + 1):
        bins[i] += bins[i - 1]

    sorted_list = [0] * len(lst)

    for i in range(len(lst) - 1, -1, -1):
        sorted_list[bins[lst[i]]] = lst[i]
        bins[lst[i]] -= 1
    return sorted_list
