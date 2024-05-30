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
        ret = []
        n = len(candidates)

        def recursive(prefix, s, target):
            if target < 0:
                return
            elif target == 0:
                ret.append(prefix)
            else:
                for i in range(s, n):
                    num = candidates[i]
                    recursive(prefix + [num], i, target - num)

        for i in range(n):
            num = candidates[i]
            recursive([num], i, target - num)
        return ret


solution = Solution().combinationSum
solution(candidates=[2, 3, 6, 7], target=7)
solution(candidates=[2, 3, 5], target=8)
solution(candidates=[2], target=1)
