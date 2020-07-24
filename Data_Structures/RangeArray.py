from Algorithms.SearchInArray import findMax
from Algorithms.Sort.LinearSort import *


class RangeArray:
    def __init__(self, lst=None):
        self.__k = findMax(lst)
        self.__units = [0] * (self.__k + 1)
        self.__total_units = [0] * (self.__k + 1)
        self.set_units_list(lst)
        self.set_total_units_list()

    # ___________________________ Query ______________________________________
    def get_num_of_entries(self, a, b):
        """
        Get how many entries there are in the range of [a,b]
        :param a: start range
        :param b: end range
        :return: int of how many entries there are in the range of [a,b]
        """
        # fix limits.
        if a < 0:
            a = 0
        if b > self.__k:
            b = self.__k

        return self.__total_units[b] - self.__total_units[a] + self.__units[a]

    # ___________________________ Build - O(n+k) _____________________________
    def set_units_list(self, lst):
        """
        Set the units list
        :param lst:
        :return:
        """
        for num in lst:
            self.__units[num] += 1
            self.__total_units[num] += 1

    def set_total_units_list(self):
        """
        Init the total units list.
        :return:
        """
        for i in range(1, self.k + 1):
            self.__total_units[i] += self.__total_units[i - 1]
