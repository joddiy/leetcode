import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n:
            ret += n % 2
            n = n >> 1
        return ret


solution = Solution().hammingWeight
solution(n=11)
solution(n=128)
