class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        s = sum(nums)
        if S > 1000 or len(nums) == 0 or S > s:
            return 0
        if len(nums) == 1:
            if S == nums[0] or S == -nums[0]:
                return 1
            else:
                return 0
        matrix = [{j: 0 for j in range(-s, s+1)} for i in range(len(nums))]
        matrix[0][nums[0]] += 1
        matrix[0][-nums[0]] += 1
        for i in range(1, len(nums)):
            for j in range(-s, s+1):
                a = 0
                b = 0
                if j-nums[i] <= s and j-nums[i] >= -s:
                    a = matrix[i-1][j-nums[i]]
                if j+nums[i] <= s and j+nums[i] >= -s:
                    b = matrix[i-1][j+nums[i]]
                matrix[i][j] = a + b
        return matrix[-1][S]

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        s = sum(nums)
        n, m = len(nums), 2 * s + 1
        if s < S: return 0
        
        dp = [[0] * m for _ in range(n + 1)]
        dp[0][s] = 1

        for i in range(n):
            for j in range(nums[i], m - nums[i]):
                if dp[i][j]:
                    dp[i + 1][j + nums[i]] += dp[i][j]
                    dp[i + 1][j - nums[i]] += dp[i][j]

        return dp[-1][s + S]


Solution().findTargetSumWays([2,7,9,13,27,31,37,3,2,3,5,7,11,13,17,19,23,29,47,53], 37)
