import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        base, ret = 1, 0
        while base < n:
            base *= 5
            ret += n // base
        return ret


solution = Solution().trailingZeroes
solution(n=3)
solution(n=5)
solution(n=0)
solution(n=30)
