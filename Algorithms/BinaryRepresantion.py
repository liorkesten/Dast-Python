from Data_Structures.my_doubly_linked_list import *


def binaryRep(n):
    """
    Function that gets an int number and return a linked list the represent the
    number in binary representation

                Time complexity: log(n)
    :param n: integer number
    :return: linked list - binary representation of n
    """
    # Create list of k pows of 2 s.t 2^k>n
    len_span = 0
    #  Edge case
    # if len_span == 0:
    #     len_span = 1
    while 2 ** len_span <= n: len_span += 1
    span = [2 ** i for i in range(len_span)]

    # Add to linked list the binary rep of n
    bin_rep = MyLinkedList()
    for i in range(len(span) - 1, -1, -1):
        if n >= span[i]:
            n -= span[i]
            bin_rep.push(1)
        else:
            bin_rep.push(0)

    return bin_rep


def addOne(L):
    """
    Gets a linked list the represent num and increase the num by one
                Time complexity : Log(n)
    :param L: Linked list the represent a num
    :return: None - change the current Linked list
    """
    cur = L.tail
    while cur:
        if cur.data == 1:
            cur.data = 0
        else:  # Cur.data = 0
            cur.data = 1
            break
        cur = cur.prev
    else:
        L.push(1)


def decreaseOne(L):
    """
    Gets a linked list the represent num and decrease the num by one
    :param L: Linked list the represent a num
    :return: None - change the current Linked list
    """
    cur = L.tail
    while cur:
        if cur.data == 0:
            cur.data = 1
        else:  # Cur.data = 1
            cur.data = 0
            break
        cur = cur.prev
    # In case that we have to delete the last pow.
    # For ex decrease 8 - 1,0,0,0  --> 0,1,1,1 --> 1,1,1
    if L.head.data == 0:
        L.head = L.head.next
        L.len -= 1


def createRepByAddOne(n):
    """
    Function that create a binary representation by adding one to linked list:
                        Time complexity: O(n)
    :param n:
    :return:
    """
    l = binaryRep(0)
    for i in range(n):
        addOne(l)
    return l
