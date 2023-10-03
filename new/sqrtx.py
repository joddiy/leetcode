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

        def recursive(i, j):
            if j < i:
                return j
            m = (i + j) // 2
            m_ = m * m
            if m_ == x:
                return m
            elif m_ > x:
                return recursive(i, m - 1)
            else:
                return recursive(m + 1, j)

        return recursive(0, x)


solution = Solution().mySqrt
# solution(x=4)
# solution(x=8)
# solution(x=1)
solution(x=6)
