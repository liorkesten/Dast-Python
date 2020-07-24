from Algorithms.LinearSort import *
from Data_Structures.MyStack import MyStack

NUM_OF_CHARS_LOWER_CASE = 26
ASCII_NUM_FIRST_CHAR = ord("a")
PARENTHESES = {
    '{': '}',
    '(': ')',
    '[': ']',
}


def areAnagrams(s, t):
    """
    Check if two strings are anagrams to each other
    :param s: First string
    :param t: Second string
    :return: True or False if the strings are anagrams
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


def parenthesesChecker(s):
    """
    Gets an string and return True or False if the string is valid parentheses
                Time complexity : O(n)
    :param s: parentheses string
    :return: True or False if the string is valid parentheses
    """
    # Create new stack
    new_stack = MyStack()

    for p in s:
        if p in PARENTHESES:
            new_stack.push(p)
        else:
            if new_stack.isStackEmpty() or \
                    PARENTHESES[new_stack.pop()] != p:
                return False
    return new_stack.isStackEmpty()
