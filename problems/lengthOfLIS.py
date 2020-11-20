from tools import *


class Solution(object):
    # O(n^2)
    @print_
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    # O(nlogn)
    # Note: dpdp array does not result in longest
    # increasing subsequence, but length of dp
    # array will give you length of LIS.
    # Consider the example:
    # input: [0, 8, 4, 12, 2]
    # dp: [0]
    # dp: [0, 8]
    # dp: [0, 4]
    # dp: [0, 4, 12]
    # dp: [0, 2, 12] which is not the longest increasing
    # subsequence, but length of dpdp array results in
    # length of Longest Increasing Subsequence.
    # 1. each time find the first one which is larger than
    # the current number to replace
    # 2. if the number is larger than anyone, just append at
    # the end
    @print_
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        size = 0
        for n in nums:
            # binary search
            i, j = 0, size
            while i < j:
                m = (i + j) // 2
                if dp[m] < n:
                    i = m + 1
                else:
                    j = m  # not m-1, since we still need m later
            dp[i] = n
            size = max(size, i + 1)
        return size


solution = Solution().lengthOfLIS

# solution([10, 9, 2, 5, 3, 7, 101, 18])
solution([10, 9, 2, 5, 3, 4])
