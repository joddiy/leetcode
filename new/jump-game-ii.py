import pprint

from tools import *


class Solution(object):
    @print_
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_max = new_max = max_s = 0
        for i, s in enumerate(nums):
            if i > last_max:
                last_max = new_max
                max_s += 1
            new_max = max(new_max, i + s)
        return max_s


solution = Solution().jump
solution([2, 3, 1, 1, 4])
solution([2, 3, 0, 1, 4])
