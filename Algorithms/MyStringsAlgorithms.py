from Algorithms.LinearSort import *
from Data_Structers.MyStack import MyStack

NUM_OF_CHARS_LOWER_CASE = 26
ASCII_NUM_FIRST_CHAR = ord("a")
OPENS = ["{", "(", "["]
CLOSES = ["}", ")", "]"]

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


def parenthesesChecker(s):
    """
    Gets an string and return True or False if the string is valid parentheses
    :param s: parentheses string
    :return: True or False if the string is valid parentheses
    """
    # Create new stack
    newStack = MyStack()

    for i in range(len(s)):
        if s[i] in OPENS:
            newStack.push(s[i])
        else:
            if newStack.isStackEmpty() or newStack.pop() != \
                    OPENS[CLOSES.index(s[i])]:
                return False
    return newStack.isStackEmpty()
