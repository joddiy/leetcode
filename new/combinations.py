import math
import pprint
import sys

from tools import *
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

        def recursive(cur_ret, start_val, cur_idx):
            if cur_idx < k:
                for i in range(start_val, n + 1):
                    recursive(cur_ret + [i], i + 1, cur_idx + 1)
            else:
                ret.append(cur_ret)

        recursive([], 1, 0)
        return ret


solution = Solution().combine
solution(n=4, k=2)
solution(n=1, k=1)
