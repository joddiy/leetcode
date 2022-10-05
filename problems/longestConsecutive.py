from tools import *


class Solution(object):
    @print_
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums_ = set(nums)
        ret = 0
        for i in nums:
            if i - 1 in nums_:
                continue
            len_ = 0
            while i in nums_:
                i += 1
                len_ += 1
            ret = max(ret, len_)
        return ret


solution = Solution().longestConsecutive

solution([100, 4, 200, 1, 3, 2])
solution([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
