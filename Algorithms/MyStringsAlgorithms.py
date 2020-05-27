from Algorithms.LinearSort import *

NUM_OF_CHARS_LOWER_CASE = 26
ASCII_NUM_FIRST_CHAR = 97


def areAnagrams(s, t):
    """

    :param s:
    :param t:
    :return:
    """
    if len(s) != len(t):
        return False

    char_counter = [0] * NUM_OF_CHARS_LOWER_CASE
    try:
        for i in range(len(s)):
            char_counter[ord(s[i]) - ASCII_NUM_FIRST_CHAR] += 1
            char_counter[ord(t[i]) - ASCII_NUM_FIRST_CHAR] -= 1
    except IndexError:
        raise Exception("The string must be string of lower case")

    return all([c == 0 for c in char_counter])
