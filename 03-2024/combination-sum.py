import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(candidates)
        ret = []

        def recursive(prefix, s, remaining):
            if remaining < 0:
                return
            elif remaining == 0:
                ret.append(prefix)
            else:
                for i in range(s, n):
                    c = candidates[i]
                    recursive(prefix + [c], i, remaining - c)

        for i, c in enumerate(candidates):
            recursive([c], i, target - c)

        return ret


solution = Solution().combinationSum
solution(candidates=[2, 3, 6, 7], target=7)
solution(candidates=[2, 3, 5], target=8)
solution(candidates=[2], target=1)
