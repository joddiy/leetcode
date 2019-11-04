from utils.tools import print_array


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        dp = [[0, 0] for _ in range(len(nums))]
        if nums[0] < 0:
            dp[0][0] = nums[0]
        else:
            dp[0][1] = nums[0]

        max_ret = dp[0][1]
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                dp[i][1] = max(nums[i], dp[i-1][1]*nums[i])
                dp[i][0] = dp[i-1][0]*nums[i]
            else:
                dp[i][1] = dp[i-1][0]*nums[i]
                dp[i][0] = min(nums[i], dp[i-1][1]*nums[i])
            max_ret = max(max_ret, dp[i][1])
        return max_ret


Solution().maxProduct([2, -1, 1, 1])
