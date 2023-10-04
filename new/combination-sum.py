import math
import pprint
import sys

from tools import *
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

        def recursive(cur_ret, cur_sum, idx):
            if cur_sum < target:
                for i in range(idx, n):
                    _n = candidates[i]
                    recursive(cur_ret + [_n], cur_sum + _n, i)
            elif cur_sum == target:
                ret.append(cur_ret)

        recursive([], 0, 0)
        return ret


solution = Solution().combinationSum
solution(candidates=[2, 3, 6, 7], target=7)
solution(candidates=[2, 3, 5], target=8)
solution(candidates=[2], target=1)
