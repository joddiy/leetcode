from tools import *


class Solution(object):
    @print_
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ret = []

        def recursive(cur, s):
            ret.append(cur)
            for i in range(s, n):
                recursive(cur + [nums[i]], i + 1)
        recursive([], 0)
        return ret


solution = Solution().subsets

solution([1, 2, 3])
solution([])