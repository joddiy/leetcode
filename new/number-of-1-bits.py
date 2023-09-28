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
        while n > 0:
            if n % 2 == 1:
                ret += 1
            n = n >> 1
        return ret


solution = Solution().hammingWeight
solution(n=5)
solution(n=8)
solution(n=7)
