# -*- coding: utf-8 -*-
# file: hammingDistance.py
# author: joddiyzhang@gmail.com
# time: 2018/11/20 5:59 PM
# ------------------------------------------------------------------------

class Solution(object):
    # def hammingDistance(self, x, y):
    #     """
    #     :type x: int
    #     :type y: int
    #     :rtype: int
    #     """
    #     return bin(x ^ y).count('1')

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        print(bin(x))
        print(bin(y))
        x = x ^ y  # the number of one
        y = 0
        print(bin(x))
        while x:
            y += 1
            print(bin(x), bin(x - 1))  # x - 1 recursively rent a one from upper bit.
            x = x & (x - 1)
        return y


print(Solution().hammingDistance(12, 11))
