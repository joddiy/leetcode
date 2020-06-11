import sys


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def recrsion(nums, prev, cupos):
            if cupos == len(nums):
                return 0
            taken = 0
            if nums[cupos] > prev:
                taken = 1 + recrsion(nums, nums[cupos], cupos+1)
            nottaken = recrsion(nums, prev, cupos + 1)
            return max(taken, nottaken)
        return recrsion(nums, -sys.maxsize, 0)

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [[-1]*len(nums) for _ in range(len(nums)+1)]

        def recrsion(prev, cupos):
            if cupos == len(nums):
                return 0
            if memo[prev+1][cupos] >= 0:
                return memo[prev+1][cupos]
            taken = 0
            if prev < 0 or nums[cupos] > nums[prev]:
                taken = 1 + recrsion(cupos, cupos+1)
            nottaken = recrsion(prev, cupos + 1)
            memo[prev+1][cupos] = max(taken, nottaken)
            return memo[prev+1][cupos]
        return recrsion(-1, 0)

    # O(n^2)
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            max_t = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    max_t = max(max_t, dp[j])
            dp[i] = max_t + 1
        return max(dp)

    # O(nlogn)
    # the final dp is not the longest increasing subsequence, 
    # but length of dp array results in length of Longest Increasing Subsequence.
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0] * len(nums)
        size = 0
        for n in nums:
            i, j = 0, size
            while i != j:
                m = (i+j)//2
                if tails[m] < n:
                    i = m + 1
                else:
                    j = m
            tails[i] = n # replace first value which is larger than n
            size = max(size, i+1) #
        return size


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
