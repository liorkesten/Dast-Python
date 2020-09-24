def selection_sort(lst, last):
    """
    Selection Sorting_Algorithms.
                      Complexity Time: O(N^2)
    :param lst:
    :param last:
    :return:
    """
    if not last:  # Base Case
        return

    max_item_index = 0
    # Find the max item in the list and keep the index.
    for i, item in enumerate(lst[:last]):
        if item > lst[max_item_index]:
            max_item_index = i

    # swap the maximum with the last element
    lst[last - 1], lst[max_item_index] = lst[max_item_index], lst[last - 1]
    # Recursive call
    selection_sort(lst, last - 1)