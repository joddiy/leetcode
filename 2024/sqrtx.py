import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        def find(i, j):
            if j < i:
                return j
            else:
                m = (i + j) // 2
                m_ = m ** 2
                if m_ == x:
                    return m
                elif m_ < x:
                    return find(m + 1, j)
                else:
                    return find(i, m - 1)
        return find(0, x)


solution = Solution().mySqrt
solution(x=4)
solution(x=8)
