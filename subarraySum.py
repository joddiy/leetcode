class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = sum(nums)
        n, m = len(nums), 2 * k + 1

        dp = [[0, 0] * m for _ in range(n + 1)]
        dp[0][nums[0]] = 1

        for i in range(n):
            for j in range(nums[i], m - nums[i]):
                if dp[i][j]:
                    dp[i + 1][j - nums[i]] += dp[i][j]
                    dp[i + 1][j] += dp[i][j]

        return dp[-1][s + k]
        
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash_map = {0: 1}
        curr_sum = 0
        ret = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            offset = curr_sum - k
            if offset in hash_map:
                ret += hash_map[offset]
            if curr_sum in hash_map:
                hash_map[curr_sum] += 1
            else:
                hash_map[curr_sum] = 1
        return ret

print(Solution().subarraySum([1, 1, 1], 2))
