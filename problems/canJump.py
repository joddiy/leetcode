from tools import *


class Solution(object):
    @print_
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_ = nums[0]
        i = 0
        while i <= max_:
            max_ = max(max_, i + nums[i])
            if max_ >= len(nums) - 1:
                return True
            i += 1
        return False


solution = Solution().canJump

solution([2, 3, 1, 1, 4])
solution([3, 2, 1, 0, 4])
solution([2])
solution([0])
solution([1, 2, 3])
