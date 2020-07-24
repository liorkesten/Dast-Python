from Data_Structures.MyStack import MyStack

PARENTHESES = {
    '{': '}',
    '(': ')',
    '[': ']',
}



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
