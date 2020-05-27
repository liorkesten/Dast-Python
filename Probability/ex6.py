# from functools import reduce
#
# birthdays = [(365 - x) / 365 for x in range(23)]
# print(birthdays)
# p_23 = reduce(lambda x, y: x * y, birthdays)
# print(p_23)

def _helper(char_list, n, word=""):
    if len(word) == n:
        print(word)
    else:
        for ch in char_list:
            _helper(char_list, n, word + ch)


def print_sequences(char_list, n):
    _helper(char_list, n)

print_sequences("Abc",10)