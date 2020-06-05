from utils.tools import print_array


class Solution(object):

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_sum = sum(nums)
        if num_sum%2 != 0:
            return False
        num_sum = num_sum//2
        if num_sum < max(nums):
            return False
        m = len(nums)
        dp = [[0] * num_sum for i in range(m)]

        for i in range(m):
            dp[i][nums[i]-1] = 1
            if nums[i]-1 == num_sum-1:
                return True

        for i in range(1,  m):
            for j in range(num_sum):
                if dp[i-1][j] == 1:
                    dp[i][j] = 1
                if j-nums[i] >= 0 and dp[i-1][j-nums[i]] == 1:
                    dp[i][j] = 1
                    if j == num_sum-1:
                        return True
        return False

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)[::-1]
        s = sum(nums)
        if s % 2 != 0:
            return False
        return self.helper(nums, s//2)

    def helper(self, nums, target):
        for i, num in enumerate(nums):
            if num > target:
                return False
            if num == target:
                return True
            if num < target:
                if self.helper(nums[i+1:], target-num):
                    return True
        return False


print(Solution().canPartition(
    [66, 90, 7, 6, 32, 16, 2, 78, 69, 88, 85, 26, 3, 9, 58, 65, 30, 96, 11, 31, 99, 49, 63, 83, 79, 97, 20, 64, 81, 80, 25, 69, 9, 75, 23, 70, 26, 71, 25, 54, 1, 40, 41, 82, 32, 10, 26, 33, 50, 71, 5, 91, 59, 96, 9, 15, 46, 70, 26, 32, 49, 35, 80, 21, 34, 95, 51, 66, 17, 71, 28, 88, 46, 21, 31, 71, 42, 2, 98, 96, 40, 65, 92, 43, 68, 14, 98, 38, 13, 77, 14, 13, 60, 79, 52, 46, 9, 13, 25, 8]))
