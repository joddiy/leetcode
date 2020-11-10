from tools import *


class Solution(object):
    @print_
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)


solution = Solution().missingNumber

# solution([3, 0, 1])
# solution([0, 1])
# solution([9, 6, 4, 2, 3, 5, 7, 0, 1])
# solution([0])
# solution([1])
solution([1, 2])
