from tools import *


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

        def recusive(prefix, start, target):
            if target == 0:
                ret.append(prefix)
            elif target > 0:
                for i in range(start, n):
                    num = candidates[i]
                    recusive(prefix + [num], i, target - num)

        recusive([], 0, target)
        return ret


solution = Solution().combinationSum

solution([2, 3, 6, 7], 7)
