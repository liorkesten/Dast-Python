def max_identical_dist(lst):
    """
    Gets an list of numbers and return the max distance between all numbers.
    For ex: [1,2,2,1,1] ---> 3 (from 1 at [0] to 1 at [3])
    :param lst: list
    :return: int that represent the distance between 2 identical values.
    """
    max_dist = float("-inf")
    table = dict()
    for i, val in enumerate(lst):
        if val in table and i - table[val] > max_dist:
            max_dist = i - table[val]
        table[val] = i
    return max_dist
