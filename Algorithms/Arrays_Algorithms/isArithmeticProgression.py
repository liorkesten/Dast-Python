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
