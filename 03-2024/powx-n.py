import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        minus_n = False
        if n < 0:
            minus_n = True
            n = -n

        def get(i):
            if i == 0:
                return 1
            elif i == 1:
                return x
            else:
                t = get(i // 2)
                if i % 2 == 1:
                    return t * t * x
                else:
                    return t * t

        if minus_n:
            return 1. / get(n)
        else:
            return get(n)


solution = Solution().myPow
solution(x=2.00000, n=10)
solution(x=2.10000, n=3)
solution(x=2.00000, n=-2)
