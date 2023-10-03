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

        def recusive(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            else:
                n_ = n // 2
                x_ = recusive(x, n_)
                if n % 2 == 1:
                    return x_ * x_ * x
                else:
                    return x_ * x_

        if n < 0:
            return 1. / recusive(x, -n)
        else:
            return recusive(x, n)


solution = Solution().myPow
solution(x=2.00000, n=10)
solution(x=2.00000, n=-2)
