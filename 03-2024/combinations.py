import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []

        def recursive(i, prefix):
            if len(prefix) == k:
                ret.append(prefix)
            else:
                for i in range(i, n + 1):
                    recursive(i + 1, prefix + [i])

        recursive(1, [])
        return ret


solution = Solution().combine
solution(n=4, k=2)
solution(n=1, k=1)
