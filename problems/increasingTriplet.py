from tools import *


class Solution(object):
    # O(nlog3)
    # refer to lengthOfLIS
    @print_
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [0] * len(nums)
        size = 0
        for n in nums:
            i, j = 0, size
            while i < j:
                m = (i + j) // 2
                if dp[m] < n:
                    i = m + 1
                else:
                    j = m  # not m-1, since we still need m later
            dp[i] = n
            size = max(size, i + 1)
            if size >= 3:
                return True
        return False

    # O(nlog3)
    @print_
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

solution = Solution().increasingTriplet

solution([1, 2, 3, 4, 5])
solution([5, 4, 3, 2, 1])
solution([5, 1, 5, 5, 2, 5, 4])
solution([2, 4, -2, -3])
solution([2, 1, 5, 0, 3])
